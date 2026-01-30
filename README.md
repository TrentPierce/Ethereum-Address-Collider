# Ethereum Address Collider

Developed by Trent Pierce (www.SkeeBomb.com)

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## ⚠️ IMPORTANT DISCLAIMER

**This tool is for EDUCATIONAL PURPOSES ONLY.**

The probability of finding an Ethereum address collision with a non-zero balance is astronomically low (approximately 1 in 2^160). This tool demonstrates:
- Ethereum address generation from private keys
- ECDSA cryptography implementation
- Python multiprocessing for parallel computation
- API integration with Etherscan

**Do not expect to find any wallets with funds.** This would require more computing power than exists on Earth for trillions of years.

## Description

The Ethereum Collider is a Python 3 script that repeatedly generates Ethereum wallet addresses and checks their balances using the Etherscan API. It serves as an educational tool to understand:

- How Ethereum addresses are derived from private keys
- The security of elliptic curve cryptography
- The impracticality of brute-force attacks on cryptocurrency wallets

## Features

- ✅ **Python 3 Compatible** - Fully updated for Python 3.6+
- ✅ **Pure Python Implementation** - No compiled dependencies
- ✅ **Cross-Platform** - Works on Windows, macOS, and Linux
- ✅ **Multiprocessing Support** - Uses all available CPU cores
- ✅ **Secure API Key Management** - Uses environment variables
- ✅ **Rate Limiting** - Respects Etherscan API limits
- ✅ **Error Handling** - Robust network error recovery

## Requirements

- Python 3.6 or higher
- Internet connection for API calls

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TrentPierce/Ethereum-Address-Collider.git
   cd Ethereum-Address-Collider
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Get an Etherscan API Key:**
   - Visit [https://etherscan.io/apis](https://etherscan.io/apis)
   - Create a free account
   - Generate an API key

4. **Set your API key as an environment variable:**
   
   **Linux/macOS:**
   ```bash
   export ETHERSCAN_API_KEY='your_api_key_here'
   ```
   
   **Windows (Command Prompt):**
   ```cmd
   set ETHERSCAN_API_KEY=your_api_key_here
   ```
   
   **Windows (PowerShell):**
   ```powershell
   $env:ETHERSCAN_API_KEY='your_api_key_here'
   ```

## Usage

Simply run the script:

```bash
python EthCollider.py
```

The program will:
1. Start worker processes (one per CPU core)
2. Generate random Ethereum addresses
3. Check each address balance via Etherscan API
4. Display progress in real-time
5. Alert if any address with a non-zero balance is found (extremely unlikely)

**To stop the program:**
Press `Ctrl+C`

## Random Number Generation

The script uses cryptographically secure random sources:
- **Windows:** CryptGenRandom
- **Unix-like systems:** /dev/urandom

## Technical Details

### Address Generation Process

1. Generate a random 256-bit private key
2. Calculate the corresponding public key using secp256k1 elliptic curve
3. Hash the public key with Keccak-256 (SHA3)
4. Take the last 40 characters as the Ethereum address
5. Query Etherscan API for the address balance

### Multiprocessing Architecture

- Creates one worker process per CPU core
- Each worker independently generates and checks addresses
- Inter-process communication via managed queues
- Automatic cleanup on shutdown or discovery

### Rate Limiting

- 0.2 second delay between API calls (5 requests/second max)
- Retry logic for network failures
- Respects Etherscan API rate limits

## Security Improvements

This updated version includes several security enhancements:

- ✅ **No hardcoded API keys** - Uses environment variables
- ✅ **Secure random generation** - Uses OS-provided entropy
- ✅ **Input validation** - Validates API responses
- ✅ **Error handling** - Graceful failure on network issues

## File Structure

```
Ethereum-Address-Collider/
├── EthCollider.py          # Main script
├── lib/
│   ├── ECDSA_BTC.py        # ECDSA implementation
│   ├── ECDSA_256k1.py      # secp256k1 curve parameters
│   ├── python_sha3.py      # Keccak/SHA3 implementation
│   ├── G_Table             # Pre-computed elliptic curve points
│   └── humtime.py          # Time formatting utilities
├── README.md               # This file
├── LICENSE                 # GPL v3 License
└── CODE_OF_CONDUCT.md      # Community guidelines
```

## Output

If a wallet with a balance is found (statistically impossible), the script will:
- Display the address, private key, and balance
- Save details to `priv.prv`
- Create a timestamped backup file
- Automatically terminate all worker processes

## Educational Value

This project demonstrates:

1. **Cryptographic Principles:**
   - Elliptic Curve Cryptography (ECC)
   - Key derivation
   - Hash functions (SHA-256, Keccak-256)

2. **Programming Concepts:**
   - Multiprocessing in Python
   - API integration
   - Error handling and retry logic
   - Process synchronization

3. **Blockchain Security:**
   - The computational infeasibility of brute-force attacks
   - Why 256-bit keys are considered secure
   - Address generation process in Ethereum

## Performance

On a modern CPU:
- ~5-10 addresses per second per core (limited by API rate)
- Scales linearly with number of CPU cores
- Network latency affects throughput

**Note:** Even at 1 million addresses per second, it would take longer than the age of the universe to have a reasonable chance of finding a collision.

## Support Development

If you found this educational tool useful, consider supporting development:

**Ethereum:** `01171ab97216939Ddf49b8Ac9DFFE80b8178fcF6`

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Changelog

### Version 2.0 (2026)
- ✅ Migrated to Python 3.6+
- ✅ Implemented true multiprocessing
- ✅ Added environment variable for API key
- ✅ Added rate limiting
- ✅ Improved error handling
- ✅ Updated documentation
- ✅ Fixed all encoding issues

### Version 1.0 (2017)
- Initial release for Python 2.7

## Credits

- **ECDSA Implementation:** Based on FastSignVerify by Antoine FERRON
- **SHA3/Keccak:** Based on implementation by Moshe Kaplan
- **Original Concept:** Trent Pierce

## Legal Notice

Using this tool to access wallets that don't belong to you is illegal in most jurisdictions. This tool is provided for educational purposes only. The author takes no responsibility for misuse of this software.
