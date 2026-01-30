#!/usr/bin/env python
# coding=utf8

"""
Ethereum Address Collider - Educational Cryptography Demonstration Tool

This tool demonstrates the mathematical impossibility of finding Ethereum
address collisions through brute force. It generates random private keys,
derives their corresponding Ethereum addresses, and checks if they have
any balance.

EDUCATIONAL PURPOSE ONLY - The probability of finding a collision is
approximately 1 in 2^160, making this computationally infeasible.

Copyright (C) 2017-2026  Trent Pierce
Licensed under GNU GPL v3.0

Random Sources:
    - Windows: CryptGenRandom
    - Unix/Linux: /dev/urandom
    - Both provide cryptographically secure randomness

Mathematical Background:
    - Private Key Space: 2^256 ≈ 1.16 × 10^77
    - Address Space: 2^160 ≈ 1.46 × 10^48
    - Collision Probability: Negligible (birthday paradox applies)

Cryptographic Components:
    - Elliptic Curve: secp256k1 (y² = x³ + 7)
    - Hash Functions: SHA-256, Keccak-256 (SHA3)
    - Key Derivation: ECDSA public key from private key
"""

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

# ============================================================================
# CRYPTOGRAPHIC UTILITY FUNCTIONS
# ============================================================================

def hexa(cha):
    """
    Convert an integer to a 64-character hexadecimal string.
    
    This function ensures consistent formatting of large integers as
    hex strings, which is necessary for cryptographic operations.
    The 64-character length corresponds to 256 bits (32 bytes).
    
    Args:
        cha (int): Integer to convert (typically a 256-bit number)
        
    Returns:
        str: Zero-padded hexadecimal string of exactly 64 characters
        
    Example:
        >>> hexa(255)
        '00000000000000000000000000000000000000000000000000000000000000ff'
        
    Note:
        - Removes 'L' suffix from long integers (Python 2 compatibility)
        - Pads with leading zeros to ensure 64 characters
        - Used for private keys, public key coordinates, etc.
    """
    # Convert integer to hex string, remove '0x' prefix
    hexas = hex(cha)[2:]
    
    # Remove trailing 'L' from Python 2 long integers (if present)
    if hexas.endswith('L'):
        hexas = hexas[:-1]
    
    # Pad with leading zeros to reach 64 characters (256 bits)
    while len(hexas) < 64:
        hexas = "0" + hexas
    
    return hexas


def hashrand(num):
    """
    Generate cryptographically secure random data using SHA-256.
    
    This function creates high-quality random data by:
    1. Collecting 'num' blocks of OS-level random bytes (32 bytes each)
    2. Hashing them with SHA-256 for uniform distribution
    
    The use of os.urandom() ensures cryptographic quality:
    - Windows: Uses CryptGenRandom API
    - Unix/Linux: Reads from /dev/urandom
    - Both are suitable for cryptographic applications
    
    Args:
        num (int): Number of 32-byte random blocks to generate
        
    Returns:
        str: Hexadecimal string of SHA-256 hash of random data
        
    Security Note:
        - Uses OS-level entropy sources
        - Hash provides uniform distribution
        - Suitable for cryptographic key generation
        
    Example:
        >>> random_hash = hashrand(1024)
        >>> len(random_hash)
        64  # SHA-256 produces 32 bytes = 64 hex characters
    """
    # Initialize empty byte string for random data accumulation
    rng_data = b''
    
    # Collect 'num' blocks of 32 random bytes each
    # Total entropy: num × 256 bits
    for idat in range(num):
        # os.urandom(32) provides 32 bytes (256 bits) of crypto-quality random data
        rng_data = rng_data + os.urandom(32)
    
    # Verify we collected the expected amount of random data
    assert len(rng_data) == num * 32, "Random data generation failed"
    
    # Hash all random data with SHA-256 for uniform distribution
    # This prevents any potential bias in the random source
    return hashlib.sha256(rng_data).hexdigest()


def randomforkey():
    """
    Generate a cryptographically secure random private key for secp256k1.
    
    This function generates a random integer that serves as an Ethereum
    private key. The key must fall within the valid range for the secp256k1
    elliptic curve used by Ethereum and Bitcoin.
    
    Valid Range:
        1 ≤ private_key < n
        where n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        (the order of the secp256k1 curve)
    
    Algorithm:
        1. Generate 1024 blocks of random data (32,768 bytes total)
        2. Hash with SHA-256 to get uniform 256-bit number
        3. Check if number falls in valid range [1, n)
        4. If invalid, repeat (probability of rejection: ~2^-128)
    
    Returns:
        int: Random private key in valid secp256k1 range
        
    Cryptographic Properties:
        - Uniform distribution over key space
        - Unpredictable (assuming secure OS random source)
        - Meets entropy requirements for cryptographic keys
        
    Example:
        >>> key = randomforkey()
        >>> 1 <= key < 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
        True
        
    Security Note:
        The massive amount of random data (1024 × 32 bytes) ensures
        that even if the OS random source has slight biases, the
        SHA-256 hash will produce a uniformly distributed result.
    """
    candint = 0  # Initialize candidate integer
    
    # secp256k1 curve order (maximum valid private key + 1)
    # This is a prime number defining the size of the curve
    # Any private key must be: 0 < key < r
    r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    
    # Loop until we get a valid key
    # Probability of rejection per iteration: ~2^-128 (extremely rare)
    while candint < 1 or candint >= r:
        # Generate 1024 × 32 bytes = 32,768 bytes of random data
        # Then hash to 32 bytes with uniform distribution
        cand = hashrand(1024)
        
        # Convert hex string to integer
        candint = int(cand, 16)
        
        # If candint is outside valid range [1, r), loop repeats
        # This ensures we never use key 0 (invalid) or key ≥ r (wraps around)
    
    return candint


def compute_adr(priv_num):
    """
    Compute an Ethereum address from a private key.
    
    This function implements the standard Ethereum address derivation:
    
    Step-by-Step Process:
        1. Private Key → Public Key (via elliptic curve multiplication)
        2. Public Key → Keccak-256 Hash
        3. Take last 20 bytes → Ethereum Address
    
    Mathematical Detail:
        1. Public Key = private_key × G (generator point on secp256k1)
           - This is elliptic curve point multiplication
           - Result is a point (x, y) on the curve
        
        2. Concatenate x and y coordinates (each 32 bytes = 64 bytes total)
        
        3. Hash with Keccak-256 (not standard SHA-3)
           - Ethereum uses the pre-FIPS version of SHA-3
           - Output: 32 bytes (256 bits)
        
        4. Take last 20 bytes (40 hex characters) as address
           - This is why addresses are 40 characters long
           - With 0x prefix: 0x + 40 chars = 42 characters total
    
    Args:
        priv_num (int): Private key as integer (256-bit number)
        
    Returns:
        str: Ethereum address (40 hexadecimal characters, no 0x prefix)
             Returns "x" on error
        
    Example:
        >>> private_key = 1
        >>> address = compute_adr(private_key)
        >>> len(address)
        40
        >>> all(c in '0123456789abcdef' for c in address)
        True
        
    Security Note:
        The private key is never transmitted or stored. Only the derived
        address is used for balance checking. Private keys are only saved
        if a funded address is found (which won't happen in practice).
        
    Cryptographic Properties:
        - One-way function: Cannot derive private key from address
        - Deterministic: Same private key always gives same address
        - Collision-resistant: Finding two keys with same address is infeasible
    """
    try:
        # Step 1: Derive Public Key from Private Key
        # mulG() performs elliptic curve multiplication: priv_num × G
        # where G is the secp256k1 generator point
        # Result is a point (x, y) on the elliptic curve
        public_point = mulG(priv_num)
        
        # Wrap the point in a Public_key object
        # This validates that the point is on the curve
        pubkey = Public_key(generator_256, public_point)
        
        # Step 2: Format Public Key Coordinates
        # Extract x and y coordinates and convert to 64-char hex strings
        # Each coordinate is 256 bits = 32 bytes = 64 hex characters
        x_coord = hexa(pubkey.point.x())  # X coordinate of public key
        y_coord = hexa(pubkey.point.y())  # Y coordinate of public key
        
        # Concatenate coordinates: total 128 hex characters = 64 bytes
        pubkeyhex = (x_coord + y_coord).encode('utf-8')
        
        # Convert hex string to actual bytes
        pubkeyhex_bytes = bytes.fromhex(pubkeyhex.decode('utf-8'))
        
        # Step 3: Hash with Keccak-256
        # Ethereum uses Keccak-256 (original SHA-3 submission)
        # NOT the final FIPS SHA-3 standard
        hash_result = lib.python_sha3.sha3_256(pubkeyhex_bytes).hexdigest()
        
        # Step 4: Take Last 20 Bytes (40 hex characters)
        # This is the Ethereum address
        # Why 20 bytes? Balance between collision resistance and size
        address = hash_result[-40:]
        
        return address
        
    except KeyboardInterrupt:
        # Allow graceful shutdown on Ctrl+C
        return "x"
    except Exception as e:
        # Catch any other errors (shouldn't happen with valid input)
        print(f"Error computing address: {e}")
        return "x"


# ============================================================================
# API AND NETWORK FUNCTIONS
# ============================================================================

def check_balance(address, api_key):
    """
    Check the balance of an Ethereum address using Etherscan API.
    
    This function queries the Etherscan API to check if an address has
    any balance. It includes retry logic, rate limiting, and error handling.
    
    API Details:
        - Endpoint: https://api.etherscan.io/api
        - Module: account
        - Action: balance
        - Returns: Balance in Wei (1 ETH = 10^18 Wei)
    
    Args:
        address (str): Ethereum address (40 hex characters)
        api_key (str): Etherscan API key from environment variable
        
    Returns:
        str: Balance in Wei as string, or None if error/not found
        
    Retry Logic:
        - Maximum 3 attempts
        - Exponential backoff on failures
        - Handles timeouts, network errors, rate limits
    
    Rate Limiting:
        - Etherscan free tier: 5 requests/second, 100k/day
        - This function called with 0.2s delay between calls
        - Automatic retry if rate limit hit
        
    Example:
        >>> balance = check_balance('0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0', api_key)
        >>> if balance and balance != '0':
        ...     print(f"Found wallet with {balance} Wei")
        
    Error Handling:
        - Network timeouts: Retry with backoff
        - JSON decode errors: Return None
        - Rate limiting: Wait and retry
        - API errors: Print message and continue
    """
    # Validate API key is present
    if not api_key:
        print("Warning: No API key provided. Set ETHERSCAN_API_KEY environment variable.")
        return None
    
    # Retry configuration
    max_retries = 3
    retry_delay = 1  # seconds
    
    # Attempt the API call up to max_retries times
    for attempt in range(max_retries):
        try:
            # Construct API URL
            # Format: /api?module=account&action=balance&address={addr}&tag=latest&apikey={key}
            url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}'
            
            # Make HTTP GET request with 10 second timeout
            r = requests.get(url, timeout=10)
            
            # Raise exception for HTTP errors (4xx, 5xx)
            r.raise_for_status()
            
            # Parse JSON response
            data = json.loads(r.text)
            
            # Check for rate limiting
            if data.get('status') == '0' and 'rate limit' in data.get('message', '').lower():
                print("Rate limit reached. Waiting before retry...")
                # Exponential backoff: wait longer on each retry
                time.sleep(retry_delay * (attempt + 1))
                continue  # Try again
            
            # Check for successful response
            if data.get('status') == '1':
                # Return balance as string (in Wei)
                return data.get('result', '0')
            else:
                # API returned error status
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return None
        
        except requests.exceptions.Timeout:
            # Request took longer than 10 seconds
            print(f"Request timeout (attempt {attempt + 1}/{max_retries})")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
        
        except requests.exceptions.RequestException as e:
            # Network error (connection failed, DNS error, etc.)
            print(f"Network error: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
        
        except json.JSONDecodeError as e:
            # Response wasn't valid JSON
            print(f"JSON decode error: {e}")
            return None
        
        except Exception as e:
            # Unexpected error
            print(f"Unexpected error checking balance: {e}")
            return None
    
    # All retries exhausted
    return None


# ============================================================================
# MULTIPROCESSING WORKER FUNCTION
# ============================================================================

def worker_generate_addresses(worker_id, result_queue, api_key, gtable_path):
    """
    Worker process function for parallel address generation and checking.
    
    This function runs in a separate process and continuously:
    1. Generates random private keys
    2. Derives Ethereum addresses
    3. Checks balances via API
    4. Reports progress to main process
    5. Terminates if balance found or interrupted
    
    Multiprocessing Architecture:
        - Each worker is an independent process
        - Workers communicate via a shared Queue
        - Main process aggregates results
        - Graceful shutdown on Ctrl+C
    
    Args:
        worker_id (int): Unique identifier for this worker (0 to N-1)
        result_queue (multiprocessing.Queue): Thread-safe queue for results
        api_key (str): Etherscan API key
        gtable_path (str): Path to pre-computed elliptic curve table
        
    Queue Message Types:
        - 'progress': Regular updates on addresses checked
        - 'found': Wallet with balance discovered
        - 'error': Worker encountered an error
        - 'stopped': Worker stopped by user
        
    Example Queue Message:
        {
            'type': 'progress',
            'worker_id': 2,
            'count': 150
        }
        
    Performance:
        - Each worker processes ~5 addresses/second (API limited)
        - 8 workers = ~40 addresses/second
        - Rate limiting ensures API compliance
        
    Security Note:
        - Private keys generated in isolated process memory
        - Keys discarded immediately if balance is 0
        - Only saved if balance found (won't happen)
    """
    # Load pre-computed elliptic curve table for this worker
    # Each worker needs its own copy in its memory space
    load_gtable(gtable_path)
    
    # Track how many addresses this worker has checked
    addresses_checked = 0
    
    try:
        # Main worker loop - runs until balance found or interrupted
        while True:
            # STEP 1: Generate random private key
            # Uses cryptographically secure randomness
            privkeynum = randomforkey()
            
            # STEP 2: Derive Ethereum address from private key
            # This performs elliptic curve multiplication and hashing
            address = compute_adr(privkeynum)
            
            # Skip if address computation failed
            if address == "x":
                continue
            
            # Increment counter
            addresses_checked += 1
            
            # STEP 3: Check if address has any balance
            # This makes an API call to Etherscan
            balance = check_balance(address, api_key)
            
            # STEP 4: Rate limiting
            # Wait 0.2 seconds between API calls (5 requests/second max)
            # This respects Etherscan's free tier rate limit
            time.sleep(0.2)
            
            # STEP 5: Report progress periodically
            # Send update every 10 addresses to avoid queue overflow
            if addresses_checked % 10 == 0:
                result_queue.put({
                    'type': 'progress',
                    'worker_id': worker_id,
                    'count': addresses_checked
                })
            
            # STEP 6: Check if balance was found
            # This will (almost certainly) never happen
            # Probability: ~1 in 2^160 per address checked
            if balance and balance != '0':
                # Convert private key to hex string
                pvhex = hexa(privkeynum)
                
                # Send success message to main process
                result_queue.put({
                    'type': 'found',
                    'address': address,
                    'private_key': pvhex,
                    'balance': balance,
                    'worker_id': worker_id
                })
                
                # Terminate this worker (found wallet)
                break
    
    except KeyboardInterrupt:
        # User pressed Ctrl+C - graceful shutdown
        result_queue.put({
            'type': 'stopped',
            'worker_id': worker_id,
            'count': addresses_checked
        })
    
    except Exception as e:
        # Unexpected error in worker
        result_queue.put({
            'type': 'error',
            'worker_id': worker_id,
            'error': str(e)
        })


# ============================================================================
# USER INTERFACE FUNCTIONS
# ============================================================================

def print_banner():
    """
    Display application banner and disclaimer.
    
    This function prints:
    - Project name and author
    - Donation address
    - Educational purpose warning
    - Mathematical reality disclaimer
    """
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
    """
    Save discovered private key and wallet information to files.
    
    Creates two files:
    1. priv.prv - Importable private key file (overwrite protection)
    2. found_wallet_YYYYMMDD-HHMMSS.txt - Timestamped backup
    
    Args:
        pvhex (str): Private key as 64-character hex string
        address (str): Ethereum address (40 hex characters)
        balance (str): Balance in Wei
        
    Security Note:
        - Only called if balance found (won't happen)
        - Asks confirmation before overwriting existing priv.prv
        - Creates timestamped backup automatically
    """
    privfileexist = False
    conf = "n"
    
    # Check if priv.prv already exists
    if os.path.isfile('priv.prv'):
        privfileexist = True
        conf = input("Enter 'y' to confirm overwriting priv.prv file : ")
    
    # Save to priv.prv if confirmed or doesn't exist
    if conf == "y" or not privfileexist:
        with open('priv.prv', 'w') as f:
            f.write(pvhex)
        print("Private key exported in priv.prv file")
        print("Can be imported in geth : 'geth account import priv.prv'\n")
    
    # Also save to timestamped file (always)
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"found_wallet_{timestamp}.txt"
    with open(filename, 'w') as f:
        f.write(f"Wallet Found!\n")
        f.write(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Private Key: {pvhex}\n")
        f.write(f"Balance (Wei): {balance}\n")
    print(f"Details also saved to {filename}")


# ============================================================================
# MAIN PROGRAM
# ============================================================================

if __name__ == '__main__':
    """
    Main program execution.
    
    Flow:
        1. Validate API key from environment
        2. Display banner and warnings
        3. Load cryptographic tables
        4. Start worker processes
        5. Monitor results
        6. Handle graceful shutdown
    """
    
    # STEP 1: Get API key from environment variable (security best practice)
    api_key = os.getenv('ETHERSCAN_API_KEY', '')
    
    # Validate API key is set
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
    
    # STEP 2: Display banner and educational warnings
    print_banner()
    
    # STEP 3: Load pre-computed elliptic curve table
    # This table speeds up point multiplication on the secp256k1 curve
    gtable_path = 'lib/G_Table'
    if not os.path.exists(gtable_path):
        print(f"ERROR: {gtable_path} not found!")
        sys.exit(1)
    
    load_gtable(gtable_path)
    
    # STEP 4: Determine optimal number of worker processes
    # Use one process per CPU core for maximum parallelism
    num_processes = multiprocessing.cpu_count()
    print(f"Starting {num_processes} worker processes...")
    print()
    
    # STEP 5: Create inter-process communication queue
    # Manager() creates a server process to manage shared objects
    manager = multiprocessing.Manager()
    result_queue = manager.Queue()
    
    # STEP 6: Start worker processes
    processes = []
    for i in range(num_processes):
        # Create new process
        p = multiprocessing.Process(
            target=worker_generate_addresses,
            args=(i, result_queue, api_key, gtable_path)
        )
        
        # Start the process
        p.start()
        processes.append(p)
        print(f"Worker {i} started (PID: {p.pid})")
    
    print()
    print("Searching for addresses with balance...")
    print("Press Ctrl+C to stop")
    print()
    
    # STEP 7: Monitor results from workers
    total_checked = 0
    worker_counts = {i: 0 for i in range(num_processes)}
    found = False
    
    try:
        # Main monitoring loop
        while not found:
            # Check if any results available
            if not result_queue.empty():
                result = result_queue.get()
                
                # Handle different message types
                if result['type'] == 'progress':
                    # Update worker's address count
                    worker_counts[result['worker_id']] = result['count']
                    total_checked = sum(worker_counts.values())
                    
                    # Display progress (overwrite same line)
                    print(f"\rSearched {total_checked} addresses across {num_processes} workers", end='', flush=True)
                
                elif result['type'] == 'found':
                    # WALLET FOUND! (this will never actually happen)
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
                    # Worker encountered an error
                    print(f"\nWorker {result['worker_id']} error: {result['error']}")
                
                elif result['type'] == 'stopped':
                    # Worker was stopped
                    print(f"\nWorker {result['worker_id']} stopped after {result['count']} addresses")
            else:
                # No results yet, wait briefly
                time.sleep(0.1)
    
    except KeyboardInterrupt:
        # User pressed Ctrl+C - graceful shutdown
        print("\n\nStopping workers...")
    
    finally:
        # STEP 8: Clean up - terminate all worker processes
        for p in processes:
            # Request process termination
            p.terminate()
            
            # Wait up to 5 seconds for graceful shutdown
            p.join(timeout=5)
            
            # Force kill if still alive
            if p.is_alive():
                p.kill()
        
        # Display final statistics
        print(f"\nTotal addresses checked: {total_checked}")
        print("Shutdown complete.")
