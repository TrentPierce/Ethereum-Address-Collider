# Upgrade Guide: v1.0 to v2.0

This guide helps you upgrade from Ethereum Address Collider v1.0 (Python 2.7) to v2.0 (Python 3.6+).

## 🎯 Quick Start

If you just want to get v2.0 running quickly:

```bash
# 1. Pull the latest changes
git pull origin master

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key
export ETHERSCAN_API_KEY='your_api_key_here'

# 4. Run the script
python3 EthCollider.py
```

---

## 📋 What's Changed

### Major Changes

1. **Python 3 Required**: Python 2.7 is no longer supported
2. **API Key Configuration**: Must use environment variable (no more hardcoded key)
3. **True Multiprocessing**: Now actually uses multiple CPU cores
4. **Enhanced Error Handling**: Better recovery from network issues

### New Features

- ✅ Parallel address generation across all CPU cores
- ✅ Real-time progress tracking
- ✅ Automatic retry on network failures
- ✅ Rate limiting to respect API terms
- ✅ Timestamped output files

---

## 🔧 Step-by-Step Migration

### Step 1: Check Python Version

**Check your current Python version:**
```bash
python3 --version
```

**Required:** Python 3.6 or higher

**If you need to install Python 3:**
- **Ubuntu/Debian**: `sudo apt-get install python3 python3-pip`
- **macOS**: `brew install python3`
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

### Step 2: Update Dependencies

**v1.0 (old way):**
```bash
# No requirements file, manual installation
pip install requests
```

**v2.0 (new way):**
```bash
# Use requirements.txt
pip install -r requirements.txt
```

### Step 3: Configure API Key

**v1.0 (old way - INSECURE):**
```python
# Hardcoded in source code - DON'T DO THIS!
apikey=V7GSGSMWZ2CZH1B6MBXM84SZ1XG4DXDCW9
```

**v2.0 (new way - SECURE):**

1. Get a free API key from [Etherscan](https://etherscan.io/apis)

2. Set environment variable:

   **Linux/macOS (temporary):**
   ```bash
   export ETHERSCAN_API_KEY='your_key_here'
   ```

   **Linux/macOS (permanent - add to ~/.bashrc or ~/.zshrc):**
   ```bash
   echo "export ETHERSCAN_API_KEY='your_key_here'" >> ~/.bashrc
   source ~/.bashrc
   ```

   **Windows Command Prompt:**
   ```cmd
   set ETHERSCAN_API_KEY=your_key_here
   ```

   **Windows PowerShell:**
   ```powershell
   $env:ETHERSCAN_API_KEY='your_key_here'
   ```

   **Windows (permanent):**
   - Right-click "This PC" → Properties
   - Advanced system settings → Environment Variables
   - Add new user variable: `ETHERSCAN_API_KEY` = `your_key_here`

3. **Optional**: Create a `.env` file (copy from `.env.example`):
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

### Step 4: Update Your Usage

**v1.0 (old way):**
```bash
python EthCollider.py  # Python 2.7
```

**v2.0 (new way):**
```bash
python3 EthCollider.py  # Python 3.6+
```

---

## 🔄 Code Changes Reference

If you modified the v1.0 code and need to update your changes:

### Print Statements
```python
# Old (Python 2)
print 'Hello'
print 'Value:', value

# New (Python 3)
print('Hello')
print('Value:', value)
```

### Range Function
```python
# Old (Python 2)
for i in xrange(100):
    pass

# New (Python 3)
for i in range(100):
    pass
```

### Input Function
```python
# Old (Python 2)
answer = raw_input("Question? ")

# New (Python 3)
answer = input("Question? ")
```

### Long Integers
```python
# Old (Python 2)
big_num = 0xFFFFFFFFFFFFFFFFL

# New (Python 3)
big_num = 0xFFFFFFFFFFFFFFFF
```

### String/Bytes Encoding
```python
# Old (Python 2)
hex_string = data.encode('hex')
binary_data = hex_str.decode('hex')

# New (Python 3)
hex_string = data.hex()
binary_data = bytes.fromhex(hex_str)
```

### Exception Raising
```python
# Old (Python 2)
raise ValueError, "Error message"

# New (Python 3)
raise ValueError("Error message")
```

---

## 📊 Performance Comparison

### v1.0 (Single Core)
- Uses 1 CPU core
- Checks ~5 addresses/second
- No parallel processing

### v2.0 (Multi-Core)
- Uses all CPU cores
- Checks ~5 addresses/second **per core**
- Example: 8-core CPU = ~40 addresses/second
- 8x performance improvement on 8-core system

---

## 🐛 Troubleshooting

### Problem: "ETHERSCAN_API_KEY environment variable not set"

**Solution:**
```bash
export ETHERSCAN_API_KEY='your_actual_api_key'
```

Make sure to replace `your_actual_api_key` with your real key from Etherscan.

### Problem: "No module named 'queue'"

This means you're still using Python 2.

**Solution:**
```bash
python3 EthCollider.py  # Use python3 explicitly
```

### Problem: "SyntaxError: invalid syntax" on print statements

You're running Python 3 code with Python 2.

**Solution:**
```bash
python3 EthCollider.py  # Use python3, not python
```

### Problem: Rate limit errors from Etherscan

The script includes rate limiting, but if you still hit limits:

**Solution:**
- The script automatically retries
- Wait a few minutes if you see rate limit messages
- Consider upgrading to a paid Etherscan API plan for higher limits

### Problem: "ModuleNotFoundError: No module named 'requests'"

**Solution:**
```bash
pip install -r requirements.txt
# or
pip3 install requests
```

---

## 🔐 Security Improvements

### Why the API Key Change?

**v1.0 Issue:**
The API key was hardcoded directly in the source code:
```python
# INSECURE - visible to anyone who views the code
'&apikey=V7GSGSMWZ2CZH1B6MBXM84SZ1XG4DXDCW9'
```

**Problems:**
- ❌ Anyone could use/abuse your API key
- ❌ Key exposed in public GitHub repository
- ❌ Can't rotate key without editing code
- ❌ Risk of rate limit exhaustion
- ❌ Violates API terms of service

**v2.0 Solution:**
```python
# SECURE - loaded from environment
api_key = os.getenv('ETHERSCAN_API_KEY', '')
```

**Benefits:**
- ✅ Key never committed to version control
- ✅ Easy to rotate keys
- ✅ Each user has their own key
- ✅ Follows security best practices
- ✅ Complies with API terms

---

## 📝 Checklist

Before running v2.0, make sure you have:

- [ ] Python 3.6+ installed
- [ ] Installed requirements: `pip install -r requirements.txt`
- [ ] Obtained Etherscan API key
- [ ] Set ETHERSCAN_API_KEY environment variable
- [ ] Tested with: `python3 EthCollider.py`

---

## 🆘 Getting Help

If you encounter issues:

1. **Check this guide** for common problems
2. **Review the README.md** for detailed usage instructions
3. **Check CHANGELOG.md** for all changes
4. **File an issue** on GitHub with:
   - Your Python version: `python3 --version`
   - Your OS: Windows/macOS/Linux
   - Error message (without your API key!)
   - Steps to reproduce

---

## 💡 Tips

### Using Virtual Environments

Recommended for Python projects:

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the script
python EthCollider.py
```

### Persistent API Key Setup

Add to your shell configuration file:

**~/.bashrc or ~/.zshrc:**
```bash
export ETHERSCAN_API_KEY='your_key_here'
```

Then reload:
```bash
source ~/.bashrc
```

---

## 🎓 Learning Resources

Understanding the changes:

- [Python 3 Migration Guide](https://docs.python.org/3/howto/pyporting.html)
- [Multiprocessing in Python](https://docs.python.org/3/library/multiprocessing.html)
- [Environment Variables](https://en.wikipedia.org/wiki/Environment_variable)
- [Ethereum Address Generation](https://ethereum.org/en/developers/docs/accounts/)

---

## ✅ Verification

Test that everything works:

```bash
# Should show Python 3.6+
python3 --version

# Should show your API key (keep it secret!)
echo $ETHERSCAN_API_KEY

# Should run without errors
python3 EthCollider.py
```

Expected output:
```
======================================================================
Ethereum Collider developed by Trent Pierce (www.SkeeBomb.com)
======================================================================
...
Starting 8 worker processes...
Worker 0 started (PID: ...)
...
```

---

**Questions?** Check the [README.md](README.md) or [open an issue](https://github.com/TrentPierce/Ethereum-Address-Collider/issues).
