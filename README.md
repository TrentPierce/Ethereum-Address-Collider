# Ethereum Address Collider

Developed by Trent Pierce ([www.SkeeBomb.com](https://www.skeebomb.com))

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Educational](https://img.shields.io/badge/purpose-educational-green.svg)](https://github.com/TrentPierce/Ethereum-Address-Collider)

---

## ⚠️ CRITICAL DISCLAIMER - READ BEFORE USE

**THIS TOOL IS FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY**

### Understanding the Mathematical Reality

The probability of finding an Ethereum address collision with funds is:

**1 in 2^160** (approximately **1.46 × 10^48** or **1,460,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000**)

### What Does This Mean?

- **If every person on Earth** (8 billion people) generated **1 trillion addresses per second**
- It would take approximately **58,000,000,000,000,000,000,000 years** (58 sextillion years)
- To have a **50% chance** of finding ONE collision
- For context: The universe is only **13.8 billion years old**

### Reality Check

> "You are more likely to be struck by lightning **1,000,000 times in a row** while simultaneously winning **every lottery on Earth** than to find a single funded Ethereum wallet through random generation."

**This tool will NEVER find a funded wallet. It demonstrates cryptographic security principles.**

---

## 📚 Table of Contents

- [Purpose](#-purpose)
- [Educational Value](#-educational-value)
- [Features](#-features)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Performance](#-performance)
- [Mathematical Analysis](#-mathematical-analysis)
- [Security Practices](#-security-practices)
- [Ethical Guidelines](#-ethical-guidelines)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎓 Purpose

This project is a **cryptographic education tool** that demonstrates:

1. **Ethereum Address Generation**: How addresses are derived from private keys
2. **Elliptic Curve Cryptography**: Implementation of secp256k1
3. **Cryptographic Hashing**: SHA-256 and Keccak-256 (SHA3) algorithms
4. **Key Space Analysis**: Why 256-bit keys are considered secure
5. **Python Multiprocessing**: Parallel computation techniques
6. **API Integration**: Working with blockchain explorers

### What This Tool Does

- Generates random 256-bit private keys using cryptographically secure randomness
- Derives Ethereum addresses using the secp256k1 elliptic curve
- Checks address balances via the Etherscan API
- Demonstrates parallel processing with Python's multiprocessing module

### What This Tool Does NOT Do

- ❌ Find funded wallets (mathematically impossible)
- ❌ "Hack" or "crack" Ethereum
- ❌ Provide any practical way to obtain cryptocurrency
- ❌ Threaten blockchain security in any way

---

## 🎯 Educational Value

### For Students & Developers

This project teaches:

**Cryptography Concepts:**
- Public key cryptography fundamentals
- Elliptic curve mathematics
- Cryptographic hash functions
- Key derivation processes
- Random number generation

**Programming Skills:**
- Python 3 multiprocessing
- API integration and error handling
- Process synchronization
- Rate limiting implementation
- Environment variable management

**Security Principles:**
- Why cryptocurrency is secure
- Key space analysis
- Brute force attack futility
- Secure coding practices

---

## ✨ Features

- ✅ **Python 3.6+ Compatible** - Modern, maintained codebase
- ✅ **Pure Python Implementation** - No compiled dependencies required
- ✅ **Cross-Platform** - Windows, macOS, Linux support
- ✅ **True Multiprocessing** - Utilizes all CPU cores efficiently
- ✅ **Secure Configuration** - Environment-based API key management
- ✅ **Rate Limiting** - Respects Etherscan API guidelines (5 req/sec)
- ✅ **Comprehensive Error Handling** - Robust network failure recovery
- ✅ **Real-Time Progress** - Live statistics across all workers
- ✅ **Educational Documentation** - Extensive code comments and guides

---

## 📦 Installation

### Prerequisites

- **Python 3.6 or higher**
- **Internet connection** for API calls
- **Etherscan API key** (free)

### Step 1: Clone the Repository

```bash
git clone https://github.com/TrentPierce/Ethereum-Address-Collider.git
cd Ethereum-Address-Collider
```

### Step 2: Install Dependencies

```bash
# Using pip
pip install -r requirements.txt

# Or using pip3 explicitly
pip3 install -r requirements.txt
```

**Dependencies:**
- `requests` - HTTP library for API calls

### Step 3: Obtain Etherscan API Key

1. Visit [Etherscan API Registration](https://etherscan.io/apis)
2. Create a free account
3. Navigate to "API Keys"
4. Generate a new API key
5. Copy your API key (keep it secret!)

**Etherscan Free Tier:**
- 5 requests per second
- 100,000 requests per day
- Perfect for educational use

---

## ⚙️ Configuration

### Environment Variable Setup

The API key must be set as an environment variable for security.

#### Linux / macOS

**Temporary (current session only):**
```bash
export ETHERSCAN_API_KEY='your_api_key_here'
```

**Permanent (add to shell profile):**
```bash
# For bash
echo 'export ETHERSCAN_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc

# For zsh
echo 'export ETHERSCAN_API_KEY="your_api_key_here"' >> ~/.zshrc
source ~/.zshrc
```

#### Windows

**Command Prompt (temporary):**
```cmd
set ETHERSCAN_API_KEY=your_api_key_here
```

**PowerShell (temporary):**
```powershell
$env:ETHERSCAN_API_KEY='your_api_key_here'
```

**Permanent (System Environment Variables):**
1. Open Start Menu → Search "environment variables"
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Variable name: `ETHERSCAN_API_KEY`
6. Variable value: Your API key
7. Click OK

#### Verify Configuration

```bash
# Linux/macOS
echo $ETHERSCAN_API_KEY

# Windows PowerShell
echo $env:ETHERSCAN_API_KEY
```

### Optional: .env File

Copy the example file and edit:
```bash
cp .env.example .env
# Edit .env with your favorite editor
nano .env
```

**⚠️ Important:** Never commit `.env` files to version control!

---

## 🚀 Usage

### Basic Usage

```bash
python3 EthCollider.py
```

### Expected Output

```
======================================================================
Ethereum Collider developed by Trent Pierce (www.SkeeBomb.com)
======================================================================

To promote development, please send donations to:
01171ab97216939Ddf49b8Ac9DFFE80b8178fcF6

WARNING: This tool is for educational purposes only.
The probability of finding a collision is astronomically low.
======================================================================

Starting 8 worker processes...
Worker 0 started (PID: 12345)
Worker 1 started (PID: 12346)
Worker 2 started (PID: 12347)
Worker 3 started (PID: 12348)
Worker 4 started (PID: 12349)
Worker 5 started (PID: 12350)
Worker 6 started (PID: 12351)
Worker 7 started (PID: 12352)

Searching for addresses with balance...
Press Ctrl+C to stop

Searched 1247 addresses across 8 workers
```

### Stopping the Program

Press **Ctrl+C** to gracefully stop all worker processes.

### Output Files

If a wallet is found (won't happen), it creates:
- `priv.prv` - Private key file
- `found_wallet_YYYYMMDD-HHMMSS.txt` - Timestamped details

---

## 🔬 How It Works

### Step-by-Step Process

#### 1. **Private Key Generation**
```
Generate 256-bit random number using OS entropy
↓
Ensure it's within valid range (1 to n-1)
↓
This is the private key
```

**Implementation:**
- Uses `os.urandom()` for cryptographically secure randomness
- Windows: Uses CryptGenRandom
- Unix/Linux: Uses /dev/urandom
- Validates range: 1 ≤ key < `secp256k1.n`

#### 2. **Public Key Derivation**
```
Private Key (scalar)
↓
Multiply by generator point G on secp256k1 curve
↓
Result: Public Key (x, y point on curve)
```

**Cryptographic Details:**
- Curve: secp256k1 (same as Bitcoin)
- Generator Point: G (predefined)
- Operation: Point multiplication (private_key × G)
- Result: 64-byte uncompressed public key

#### 3. **Address Generation**
```
Public Key (x, y coordinates)
↓
Concatenate x and y (64 bytes)
↓
Apply Keccak-256 hash
↓
Take last 20 bytes (40 hex characters)
↓
Ethereum Address
```

**Format:**
- Raw address: 40 hexadecimal characters
- Checksum version: 0x + 40 characters
- Example: `0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0`

#### 4. **Balance Check**
```
Generated Address
↓
API Request to Etherscan
↓
Parse JSON response
↓
Check if balance > 0
```

**API Endpoint:**
```
https://api.etherscan.io/api?module=account&action=balance&address={ADDRESS}&tag=latest&apikey={KEY}
```

### Parallel Processing Architecture

```
Main Process
├── Worker 0 ──> Generate → Check → Report
├── Worker 1 ──> Generate → Check → Report
├── Worker 2 ──> Generate → Check → Report
├── Worker 3 ──> Generate → Check → Report
├── Worker 4 ──> Generate → Check → Report
├── Worker 5 ──> Generate → Check → Report
├── Worker 6 ──> Generate → Check → Report
└── Worker 7 ──> Generate → Check → Report
      ↓
Result Queue (thread-safe communication)
      ↓
Main Process (aggregates and displays)
```

**Benefits:**
- Linear scaling with CPU cores
- Independent worker processes
- Shared result queue for communication
- Automatic load balancing

---

## ⚡ Performance

### Throughput

**Single Core:**
- ~5 addresses per second (API rate limited)

**Multi-Core (8 cores):**
- ~40 addresses per second
- 8x performance improvement

**Rate Limiting:**
- 0.2 second delay between API calls
- Maximum 5 requests per second per worker
- Respects Etherscan free tier limits

### Expected Performance

| CPU Cores | Addresses/Second | Addresses/Hour | Addresses/Day |
|-----------|-----------------|----------------|---------------|
| 1         | 5               | 18,000         | 432,000       |
| 2         | 10              | 36,000         | 864,000       |
| 4         | 20              | 72,000         | 1,728,000     |
| 8         | 40              | 144,000        | 3,456,000     |
| 16        | 80              | 288,000        | 6,912,000     |

**Reality Check:**
Even at **1 million addresses per second**, it would take **1.46 × 10^42 years** to check all possible addresses.

---

## 📊 Mathematical Analysis

### Key Space Size

**Ethereum Private Keys:**
- Size: 256 bits
- Total possible keys: 2^256 ≈ 1.16 × 10^77
- Valid keys (secp256k1): ~2^256

**Ethereum Addresses:**
- Size: 160 bits (derived from public key)
- Total possible addresses: 2^160 ≈ 1.46 × 10^48

### Collision Probability

Using the birthday paradox formula:

**For 50% collision chance:**
- Need to generate: √(2^160) ≈ 2^80 addresses
- That's approximately: 1.21 × 10^24 addresses

**At 1 billion addresses per second:**
- Time required: 38 billion years
- Universe age: 13.8 billion years
- Ratio: **2,754 times the age of the universe**

### Computational Infeasibility

**Current fastest supercomputer (Frontier, 2024):**
- Speed: ~1.1 exaflops (1.1 × 10^18 operations/sec)
- Assume 1 million addresses/sec (generous)

**Time to 50% collision probability:**
- 1.21 × 10^24 / (1 × 10^6) = 1.21 × 10^18 seconds
- = **38 billion years**

**Energy Considerations:**
- Estimated energy to count to 2^80: More than the sun's total output
- Physical impossibility, not just computational

### Why Cryptocurrencies Are Secure

This mathematical reality is why:
- ✅ Your cryptocurrency is safe
- ✅ 256-bit keys are considered unbreakable
- ✅ Quantum computers won't help (still exponential)
- ✅ Brute force attacks are futile

---

## 🔐 Security Practices

### This Tool Implements:

1. **Environment Variables** - No hardcoded secrets
2. **Rate Limiting** - Respects API terms of service
3. **Secure Random Generation** - Uses OS-level entropy
4. **Error Handling** - Prevents information leakage
5. **Input Validation** - Checks API responses
6. **Process Isolation** - Multiprocessing security

### Best Practices

**DO:**
- ✅ Use environment variables for API keys
- ✅ Keep dependencies updated
- ✅ Review code before running
- ✅ Use for educational purposes only
- ✅ Understand the mathematics

**DON'T:**
- ❌ Commit API keys to version control
- ❌ Share your API key publicly
- ❌ Expect to find funded wallets
- ❌ Use for illegal purposes
- ❌ Modify code without understanding

---

## ⚖️ Ethical Guidelines

### Legal Considerations

**Educational Use:**
- ✅ Running this tool to learn about cryptography
- ✅ Understanding blockchain security
- ✅ Academic research
- ✅ Security awareness training

**Illegal Use:**
- ❌ Attempting to access others' wallets
- ❌ Claiming found funds that aren't yours
- ❌ Bypassing security measures
- ❌ Unauthorized access attempts

### Responsible Use

1. **Understand the Purpose**: This is an educational demonstration
2. **Respect the Law**: Follow all applicable laws and regulations
3. **API Etiquette**: Don't abuse Etherscan's free API service
4. **Share Knowledge**: Use what you learn to educate others
5. **Report Vulnerabilities**: If you find security issues, report them responsibly

### Academic Citation

If using this in research or education:

```
Pierce, T. (2026). Ethereum Address Collider: A Cryptographic Education Tool.
GitHub. https://github.com/TrentPierce/Ethereum-Address-Collider
```

---

## 📖 Documentation

### Complete Guide Collection

- **[README.md](README.md)** - This file, overview and quick start
- **[INSTALL.md](INSTALL.md)** - Detailed installation guide
- **[SECURITY.md](SECURITY.md)** - Security practices and policies
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[CHANGELOG.md](CHANGELOG.md)** - Version history
- **[UPGRADE_GUIDE.md](UPGRADE_GUIDE.md)** - Migration from v1.0 to v2.0
- **[LICENSE](LICENSE)** - GPL v3 license text
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** - Community guidelines

### Code Documentation

All functions include comprehensive docstrings explaining:
- Purpose and functionality
- Parameters and return values
- Cryptographic operations
- Mathematical formulas
- Error handling

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for:

- Code style guidelines
- Pull request process
- Development setup
- Testing requirements
- Documentation standards

### Quick Start for Contributors

```bash
# Fork the repository
git clone https://github.com/yourusername/Ethereum-Address-Collider.git
cd Ethereum-Address-Collider

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
python3 EthCollider.py

# Submit pull request
```

---

## 💬 Support

### Getting Help

- **Issues**: [GitHub Issues](https://github.com/TrentPierce/Ethereum-Address-Collider/issues)
- **Discussions**: [GitHub Discussions](https://github.com/TrentPierce/Ethereum-Address-Collider/discussions)
- **Email**: Pierce.trent@gmail.com

### Common Issues

See [INSTALL.md](INSTALL.md#troubleshooting) for troubleshooting guide.

---

## 💰 Support Development

If you find this educational tool valuable:

**Ethereum:** `0x01171ab97216939Ddf49b8Ac9DFFE80b8178fcF6`

Your support helps maintain and improve this educational resource!

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**.

- ✅ Free to use, modify, and distribute
- ✅ Open source
- ✅ Must disclose source
- ✅ Must use same license

See [LICENSE](LICENSE) file for full text.

---

## 🙏 Acknowledgments

### Credits

- **ECDSA Implementation**: Based on FastSignVerify by Antoine FERRON
- **SHA3/Keccak**: Implementation by Moshe Kaplan
- **Python Community**: For excellent libraries and tools
- **Ethereum Foundation**: For blockchain innovation
- **Contributors**: Everyone who has improved this project

### Inspiration

This project was inspired by the need to educate people about:
- Why cryptocurrencies are secure
- How cryptographic systems work
- The mathematics behind blockchain security
- Practical Python programming

---

## 📚 Further Reading

### Cryptography

- [Elliptic Curve Cryptography](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography)
- [secp256k1 Curve](https://en.bitcoin.it/wiki/Secp256k1)
- [SHA-3 (Keccak)](https://en.wikipedia.org/wiki/SHA-3)

### Ethereum

- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf)
- [How Ethereum Addresses are Generated](https://ethereum.org/en/developers/docs/accounts/)
- [Ethereum Development Documentation](https://ethereum.org/en/developers/)

### Mathematics

- [Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem)
- [Cryptographic Key Length](https://www.keylength.com/)
- [Computational Complexity](https://en.wikipedia.org/wiki/Computational_complexity_theory)

---

## ⚠️ Final Warning

**Remember**: This tool will NEVER find a funded wallet. The mathematics make it impossible. Anyone claiming otherwise either:

1. Doesn't understand the mathematics
2. Is trying to scam you
3. Both

Use this tool to **learn**, not to try to get rich. The real value is in understanding how secure modern cryptography really is.

---

**Last Updated**: January 30, 2026  
**Version**: 2.0.0  
**Maintainer**: Trent Pierce ([@severesig](https://twitter.com/severesig))

---

*Made with ❤️ for education and learning*
