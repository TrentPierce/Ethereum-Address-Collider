#!/usr/bin/env python
# coding=utf8

# Ethereum Collider
# Copyright (C) 2017  Trent Pierce
#
# Pure Python address generator with Collision detection
#
# Random source for key generation :
# CryptGenRandom in Windows
# /dev/urandom   in Unix-like
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
# Uses python-sha3 from moshekaplan
#
# Enter optional argument : a hex string shorter than 11 chars
#

from lib.ECDSA_BTC import *
import lib.python_sha3
import requests
import json
import os
import sys
import time
import hashlib
import multiprocessing
from queue import Queue

def hexa(cha):
    """Convert integer to 64-character hex string."""
    hexas = hex(cha)[2:]
    if hexas.endswith('L'):
        hexas = hexas[:-1]
    while len(hexas) < 64:
        hexas = "0" + hexas
    return hexas

def hashrand(num):
    """Return sha256 of num times 256bits random data."""
    rng_data = b''
    for idat in range(num):
        rng_data = rng_data + os.urandom(32)
    assert len(rng_data) == num * 32
    return hashlib.sha256(rng_data).hexdigest()

def randomforkey():
    """Generate a random private key within valid range."""
    candint = 0
    r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    while candint < 1 or candint >= r:
        cand = hashrand(1024)
        candint = int(cand, 16)
    return candint

def compute_adr(priv_num):
    """Compute Ethereum address from private key."""
    try:
        pubkey = Public_key(generator_256, mulG(priv_num))
        pubkeyhex = (hexa(pubkey.point.x()) + hexa(pubkey.point.y())).encode('utf-8')
        pubkeyhex_bytes = bytes.fromhex(pubkeyhex.decode('utf-8'))
        return lib.python_sha3.sha3_256(pubkeyhex_bytes).hexdigest()[-40:]
    except KeyboardInterrupt:
        return "x"
    except Exception as e:
        print(f"Error computing address: {e}")
        return "x"

def check_balance(address, api_key):
    """Check balance of an Ethereum address using Etherscan API."""
    if not api_key:
        print("Warning: No API key provided. Set ETHERSCAN_API_KEY environment variable.")
        return None
    
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}'
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            
            data = json.loads(r.text)
            
            if data.get('status') == '0' and 'rate limit' in data.get('message', '').lower():
                print("Rate limit reached. Waiting before retry...")
                time.sleep(retry_delay * (attempt + 1))
                continue
                
            if data.get('status') == '1':
                return data.get('result', '0')
            else:
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return None
                
        except requests.exceptions.Timeout:
            print(f"Request timeout (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error checking balance: {e}")
            return None
    
    return None

def worker_generate_addresses(worker_id, result_queue, api_key, gtable_path):
    """Worker function to generate and check addresses in parallel."""
    # Load gtable for this worker process
    load_gtable(gtable_path)
    
    addresses_checked = 0
    
    try:
        while True:
            # Generate new address
            privkeynum = randomforkey()
            address = compute_adr(privkeynum)
            
            if address == "x":
                continue
            
            addresses_checked += 1
            
            # Check balance
            balance = check_balance(address, api_key)
            
            # Rate limiting: 5 requests per second max
            time.sleep(0.2)
            
            # Report progress periodically
            if addresses_checked % 10 == 0:
                result_queue.put({
                    'type': 'progress',
                    'worker_id': worker_id,
                    'count': addresses_checked
                })
            
            # If balance found, report it
            if balance and balance != '0':
                pvhex = hexa(privkeynum)
                result_queue.put({
                    'type': 'found',
                    'address': address,
                    'private_key': pvhex,
                    'balance': balance,
                    'worker_id': worker_id
                })
                break
                
    except KeyboardInterrupt:
        result_queue.put({
            'type': 'stopped',
            'worker_id': worker_id,
            'count': addresses_checked
        })
    except Exception as e:
        result_queue.put({
            'type': 'error',
            'worker_id': worker_id,
            'error': str(e)
        })

def print_banner():
    """Print application banner."""
    print('=' * 70)
    print('Ethereum Collider developed by Trent Pierce (www.SkeeBomb.com)')
    print('=' * 70)
    print()
    print('To promote development, please send donations to:')
    print('01171ab97216939Ddf49b8Ac9DFFE80b8178fcF6')
    print()
    print('WARNING: This tool is for educational purposes only.')
    print('The probability of finding a collision is astronomically low.')
    print('=' * 70)
    print()

def save_private_key(pvhex, address, balance):
    """Save found private key to file."""
    privfileexist = False
    conf = "n"
    
    if os.path.isfile('priv.prv'):
        privfileexist = True
        conf = input("Enter 'y' to confirm overwriting priv.prv file : ")
    
    if conf == "y" or not privfileexist:
        with open('priv.prv', 'w') as f:
            f.write(pvhex)
        print("Private key exported in priv.prv file")
        print("Can be imported in geth : 'geth account import priv.prv'\n")
    
    # Also save to a timestamped file
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"found_wallet_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(f"Wallet Found!\n")
        f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Private Key: {pvhex}\n")
        f.write(f"Balance (Wei): {balance}\n")
    print(f"Details also saved to {filename}")

if __name__ == '__main__':
    # Get API key from environment variable
    api_key = os.getenv('ETHERSCAN_API_KEY', '')
    
    if not api_key:
        print("=" * 70)
        print("ERROR: ETHERSCAN_API_KEY environment variable not set!")
        print("=" * 70)
        print("Please set your Etherscan API key:")
        print("  Linux/Mac: export ETHERSCAN_API_KEY='your_key_here'")
        print("  Windows:   set ETHERSCAN_API_KEY=your_key_here")
        print()
        print("Get a free API key at: https://etherscan.io/apis")
        print("=" * 70)
        sys.exit(1)
    
    print_banner()
    
    # Load gtable
    gtable_path = 'lib/G_Table'
    if not os.path.exists(gtable_path):
        print(f"ERROR: {gtable_path} not found!")
        sys.exit(1)
    
    load_gtable(gtable_path)
    
    # Determine number of processes
    num_processes = multiprocessing.cpu_count()
    print(f"Starting {num_processes} worker processes...")
    print()
    
    # Create result queue for inter-process communication
    manager = multiprocessing.Manager()
    result_queue = manager.Queue()
    
    # Start worker processes
    processes = []
    for i in range(num_processes):
        p = multiprocessing.Process(
            target=worker_generate_addresses,
            args=(i, result_queue, api_key, gtable_path)
        )
        p.start()
        processes.append(p)
        print(f"Worker {i} started (PID: {p.pid})")
    
    print()
    print("Searching for addresses with balance...")
    print("Press Ctrl+C to stop")
    print()
    
    # Monitor results
    total_checked = 0
    worker_counts = {i: 0 for i in range(num_processes)}
    found = False
    
    try:
        while not found:
            if not result_queue.empty():
                result = result_queue.get()
                
                if result['type'] == 'progress':
                    worker_counts[result['worker_id']] = result['count']
                    total_checked = sum(worker_counts.values())
                    print(f"\rSearched {total_checked} addresses across {num_processes} workers", end='', flush=True)
                
                elif result['type'] == 'found':
                    found = True
                    print("\n")
                    print("=" * 70)
                    print("WALLET WITH BALANCE FOUND!")
                    print("=" * 70)
                    print(f"Address:     {result['address']}")
                    print(f"Private Key: {result['private_key']}")
                    print(f"Balance:     {result['balance']} Wei")
                    print(f"Found by:    Worker {result['worker_id']}")
                    print("=" * 70)
                    
                    # Save the private key
                    save_private_key(
                        result['private_key'],
                        result['address'],
                        result['balance']
                    )
                    
                elif result['type'] == 'error':
                    print(f"\nWorker {result['worker_id']} error: {result['error']}")
                
                elif result['type'] == 'stopped':
                    print(f"\nWorker {result['worker_id']} stopped after {result['count']} addresses")
            else:
                time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("\n\nStopping workers...")
    
    finally:
        # Terminate all processes
        for p in processes:
            p.terminate()
            p.join(timeout=5)
            if p.is_alive():
                p.kill()
        
        print(f"\nTotal addresses checked: {total_checked}")
        print("Shutdown complete.")
