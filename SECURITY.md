# Security Policy

## Overview

This document outlines security practices, policies, and procedures for the Ethereum Address Collider project.

---

## Table of Contents

- [Purpose and Scope](#purpose-and-scope)
- [Security Practices](#security-practices)
- [Vulnerability Reporting](#vulnerability-reporting)
- [Secure Usage Guidelines](#secure-usage-guidelines)
- [Cryptographic Security](#cryptographic-security)
- [API Security](#api-security)
- [Code Security](#code-security)
- [Privacy Policy](#privacy-policy)

---

## Purpose and Scope

### Educational Tool Statement

**Ethereum Address Collider is an educational tool designed to demonstrate cryptographic principles.** It is NOT intended for:

- ❌ Unauthorized access to cryptocurrency wallets
- ❌ Breaking blockchain security
- ❌ Malicious or illegal activities
- ❌ Financial gain through collision attacks

### Security Goals

This project aims to:

1. ✅ Educate users about cryptographic security
2. ✅ Demonstrate secure coding practices
3. ✅ Follow responsible disclosure principles
4. ✅ Protect user privacy and API keys
5. ✅ Maintain code integrity and transparency

---

## Security Practices

### Implemented Security Measures

#### 1. Environment Variable Usage

**What**: API keys are never hardcoded in source code.

**Why**: Prevents accidental exposure in version control, public repositories, or logs.

**Implementation**:
```python
api_key = os.getenv('ETHERSCAN_API_KEY', '')
```

**Best Practice**:
- Never commit `.env` files
- Use `.env.example` as template
- Add `.env` to `.gitignore`

#### 2. Secure Random Number Generation

**What**: Uses operating system's cryptographically secure random source.

**Why**: Ensures unpredictability and proper entropy.

**Implementation**:
- **Unix/Linux**: `/dev/urandom`
- **Windows**: `CryptGenRandom`
- **Python**: `os.urandom(32)`

**Quality**:
```python
# Cryptographically secure
os.urandom(32)  # Returns 32 bytes of crypto-quality random data

# NOT secure (don't use for crypto)
random.randint()  # Pseudo-random, predictable
```

#### 3. Input Validation

**What**: All external inputs are validated before processing.

**Implementation**:
- API responses checked for expected format
- JSON parsing wrapped in try/except
- Type checking on critical operations
- Range validation for cryptographic values

**Example**:
```python
# Validate API response
if data.get('status') == '1':
    balance = data.get('result', '0')
else:
    # Handle error safely
    print(f"API Error: {data.get('message', 'Unknown')}")
```

#### 4. Error Handling

**What**: Comprehensive exception handling prevents information leakage.

**Why**: Prevents attackers from gathering system information through error messages.

**Implementation**:
- All network operations wrapped in try/except
- Generic error messages for users
- Detailed errors only in debug mode (if implemented)
- No sensitive data in error output

#### 5. Rate Limiting

**What**: Respects API rate limits to prevent abuse.

**Implementation**:
- 0.2 second delay between requests (5 req/sec)
- Retry logic with exponential backoff
- Daily request tracking (if needed)

**Why**: Prevents account suspension and ensures fair API usage.

#### 6. Process Isolation

**What**: Uses multiprocessing for worker isolation.

**Benefits**:
- Memory isolation between workers
- Crash in one worker doesn't affect others
- Secure inter-process communication via queues

#### 7. Secure Dependencies

**What**: Minimal dependencies, only well-maintained packages.

**Current Dependencies**:
- `requests` - HTTP library (widely used, maintained)

**Monitoring**:
- Regular security audits
- Dependency version pinning
- Automated vulnerability scanning (recommended)

---

## Vulnerability Reporting

### Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.0.x   | ✅ Yes            |
| < 2.0   | ❌ No (deprecated) |

### Reporting a Vulnerability

If you discover a security vulnerability, please follow responsible disclosure:

#### Step 1: DO NOT

- ❌ Open a public GitHub issue
- ❌ Post on social media
- ❌ Share details publicly before fix
- ❌ Exploit the vulnerability

#### Step 2: Report Privately

**Email**: Pierce.trent@gmail.com

**Subject**: `[SECURITY] Ethereum Address Collider Vulnerability`

**Include**:
1. Description of the vulnerability
2. Steps to reproduce
3. Potential impact
4. Suggested fix (if available)
5. Your contact information for follow-up

**Example Report**:
```
Subject: [SECURITY] Ethereum Address Collider Vulnerability

Description:
Found an issue in [component] that allows [attack].

Steps to Reproduce:
1. [Step 1]
2. [Step 2]
3. [Result]

Impact:
This could allow an attacker to [consequence].

Suggested Fix:
Consider implementing [solution].

Contact: your.email@example.com
```

#### Step 3: Response Timeline

- **24 hours**: Initial acknowledgment
- **72 hours**: Preliminary assessment
- **7 days**: Detailed response with timeline
- **30 days**: Fix implementation and release

#### Step 4: Credit

We will credit security researchers in:
- CHANGELOG.md
- Security advisory (if applicable)
- README acknowledgments

Unless you prefer to remain anonymous.

### Bug Bounty

Currently, we do not offer a paid bug bounty program. However:
- We deeply appreciate responsible disclosure
- We will publicly credit researchers
- We may offer donations as thanks

---

## Secure Usage Guidelines

### For Users

#### Protecting Your API Key

**DO**:
- ✅ Use environment variables
- ✅ Keep API keys private
- ✅ Use separate keys for different projects
- ✅ Rotate keys periodically
- ✅ Monitor API usage on Etherscan

**DON'T**:
- ❌ Commit API keys to Git
- ❌ Share keys publicly
- ❌ Use production keys for testing
- ❌ Hardcode keys in source files
- ❌ Log API keys

#### Checking for Key Exposure

```bash
# Search Git history for accidentally committed keys
git log -p | grep -i "api.*key"

# Use tools like git-secrets
git secrets --scan
```

If exposed:
1. Immediately rotate the key on Etherscan
2. Check API usage logs for abuse
3. Generate new key
4. Update environment variable

#### Safe Testing

```bash
# Use test API key for development
export ETHERSCAN_API_KEY='test_key_only'

# Never use real keys in CI/CD without encryption
# Use GitHub Secrets or similar
```

### For Developers

#### Code Review Checklist

Before submitting code:

- [ ] No hardcoded secrets
- [ ] Input validation present
- [ ] Error handling implemented
- [ ] No sensitive data in logs
- [ ] Dependencies up to date
- [ ] Type hints used where applicable
- [ ] Security best practices followed

#### Secure Coding Practices

**String Formatting**:
```python
# Safe - no injection possible
f"Address: {address}"

# Avoid eval() or exec() with user input
# NEVER:
eval(user_input)  # Dangerous!
```

**File Operations**:
```python
# Safe - controlled path
with open('priv.prv', 'w') as f:
    f.write(data)

# Avoid - path traversal possible
# NEVER:
with open(user_provided_path, 'w') as f:  # Dangerous!
```

**API Calls**:
```python
# Safe - uses https, validates response
response = requests.get(url, timeout=10)
if response.status_code == 200:
    data = response.json()

# Avoid - no validation
# RISKY:
data = eval(response.text)  # Dangerous!
```

---

## Cryptographic Security

### Algorithms Used

#### Elliptic Curve: secp256k1

**Properties**:
- Curve equation: y² = x³ + 7
- Order: ~2^256
- Used by: Bitcoin, Ethereum
- Security level: 128-bit (equivalent)

**Implementation**:
- Pure Python implementation
- No side-channel attacks (not constant-time, educational only)
- Uses pre-computed tables for performance

#### Hash Functions

**SHA-256**:
- 256-bit output
- Used for random number generation
- NIST standard

**Keccak-256 (SHA-3)**:
- 256-bit output  
- Used for Ethereum address derivation
- Based on sponge construction

### Cryptographic Guarantees

#### What This Tool Guarantees

✅ **Random Key Generation**:
- Keys are unpredictable
- Uniform distribution
- Sufficient entropy (256 bits)

✅ **Correct Implementation**:
- Follows Ethereum standards
- Generates valid addresses
- Proper key derivation

#### What This Tool Does NOT Guarantee

❌ **Constant-Time Operations**:
- Not protected against timing attacks
- Educational code, not production crypto library

❌ **Side-Channel Protection**:
- May leak information through cache, power, etc.
- Not suitable for high-security applications

❌ **Quantum Resistance**:
- secp256k1 is not quantum-resistant
- Shor's algorithm could theoretically break it (future quantum computers)

### Key Security Properties

**Private Key**:
- Size: 256 bits
- Range: 1 to `0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140`
- Security: 128-bit (birthday bound)

**Address**:
- Size: 160 bits (20 bytes)
- Format: Last 20 bytes of Keccak-256(public_key)
- Collision resistance: 2^160 operations

---

## API Security

### Etherscan API Usage

#### Rate Limits

**Free Tier**:
- 5 requests per second
- 100,000 requests per day

**This Tool's Limits**:
- 0.2 seconds between requests (5 req/sec)
- Respects free tier limits

#### Security Considerations

**Data Privacy**:
- Etherscan logs API requests
- Addresses checked are visible to Etherscan
- No personal data transmitted
- IP address recorded by Etherscan

**API Key Security**:
- Never shared between users
- Unique per user
- Free to generate
- Rotatable at any time

**Request Security**:
- Uses HTTPS only
- Validates SSL certificates
- Timeout protection (10 seconds)
- Retry logic for failures

### Preventing API Abuse

```python
# Implemented protections:

# 1. Rate limiting
time.sleep(0.2)  # 5 req/sec max

# 2. Timeout
requests.get(url, timeout=10)

# 3. Error handling
try:
    response = requests.get(url)
except requests.exceptions.RequestException:
    # Handle gracefully
    pass

# 4. Retry logic
for attempt in range(max_retries):
    try:
        response = requests.get(url)
        break
    except:
        time.sleep(retry_delay)
```

---

## Code Security

### Static Analysis

Recommended tools:

```bash
# Bandit - Security linter
pip install bandit
bandit -r . -ll

# Safety - Dependency checker
pip install safety
safety check

# Pylint - Code quality
pip install pylint
pylint EthCollider.py
```

### Dependency Management

**Current Policy**:
1. Minimal dependencies (only `requests`)
2. Pin major versions in requirements.txt
3. Regular updates for security patches
4. Automated scanning (recommended for future)

**Update Process**:
```bash
# Check for updates
pip list --outdated

# Update safely
pip install --upgrade requests

# Test thoroughly
python3 EthCollider.py

# Update requirements.txt
pip freeze > requirements.txt
```

### Code Signing

**Future Enhancement**:
- GPG signing of commits
- Release verification
- Checksum files for downloads

---

## Privacy Policy

### Data Collection

**This tool does NOT collect**:
- ❌ User personal information
- ❌ Generated private keys
- ❌ API keys
- ❌ Usage statistics
- ❌ Telemetry data

**This tool does access**:
- ✅ Etherscan API (you provide the key)
- ✅ Internet (for API calls only)

### Third-Party Services

**Etherscan.io**:
- Purpose: Check address balances
- Data sent: Ethereum addresses, API key
- Privacy policy: https://etherscan.io/privacy
- Note: They log API requests

### Local Data

**Stored locally** (only if wallet found):
- `priv.prv` - Private key file
- `found_wallet_*.txt` - Wallet details

**User Responsibility**:
- Protect these files
- Never share private keys
- Delete if no longer needed

---

## Compliance

### Legal Considerations

**Educational Use**: ✅ Legal
**Research**: ✅ Legal
**Learning Cryptography**: ✅ Legal

**Attempting to access others' wallets**: ❌ Illegal
**Using found keys without permission**: ❌ Illegal
**Circumventing security**: ❌ Illegal

### Ethical Use

Users must:
1. Use for educational purposes only
2. Respect intellectual property
3. Follow applicable laws
4. Not attempt unauthorized access
5. Report vulnerabilities responsibly

### Disclaimer

This software is provided "AS IS" without warranty of any kind. The author is not responsible for misuse or damages resulting from use of this software.

---

## Security Updates

### Subscribe to Updates

Watch this repository on GitHub for:
- Security advisories
- Vulnerability patches  
- Update notifications

### Changelog

All security-related changes documented in [CHANGELOG.md](CHANGELOG.md).

---

## Contact

**Security Issues**: Pierce.trent@gmail.com (private)  
**General Questions**: [GitHub Issues](https://github.com/TrentPierce/Ethereum-Address-Collider/issues) (public)  
**Discussions**: [GitHub Discussions](https://github.com/TrentPierce/Ethereum-Address-Collider/discussions)

---

## Acknowledgments

We thank the security community for responsible disclosure practices and helping keep this project secure.

---

**Last Updated**: January 30, 2026  
**Policy Version**: 1.0
