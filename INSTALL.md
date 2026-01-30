# Installation Guide

Complete installation instructions for Ethereum Address Collider v2.0+

---

## Table of Contents

- [System Requirements](#system-requirements)
- [Python Installation](#python-installation)
- [Project Installation](#project-installation)
- [API Key Setup](#api-key-setup)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Advanced Setup](#advanced-setup)

---

## System Requirements

### Minimum Requirements

- **Operating System**: Windows 7+, macOS 10.12+, or Linux
- **Python**: Version 3.6 or higher
- **RAM**: 512 MB (minimal)
- **Disk Space**: 100 MB
- **Internet**: Stable connection for API calls

### Recommended Requirements

- **Operating System**: Windows 10+, macOS 11+, or modern Linux
- **Python**: Version 3.9 or higher
- **RAM**: 2 GB or more
- **CPU**: Multi-core processor (for parallel processing)
- **Internet**: Broadband connection (>1 Mbps)

---

## Python Installation

### Check Existing Python

First, check if Python 3 is already installed:

```bash
python3 --version
```

If you see `Python 3.6` or higher, skip to [Project Installation](#project-installation).

### Ubuntu/Debian Linux

```bash
# Update package list
sudo apt update

# Install Python 3 and pip
sudo apt install python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

### Fedora/RHEL/CentOS

```bash
# Install Python 3
sudo dnf install python3 python3-pip

# Or on older systems
sudo yum install python3 python3-pip

# Verify installation
python3 --version
pip3 --version
```

### macOS

#### Option 1: Using Homebrew (Recommended)

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python 3
brew install python3

# Verify installation
python3 --version
pip3 --version
```

#### Option 2: Using Official Installer

1. Download from [python.org](https://www.python.org/downloads/macos/)
2. Run the `.pkg` installer
3. Follow installation wizard
4. Verify in Terminal: `python3 --version`

### Windows

#### Option 1: Using Official Installer (Recommended)

1. Visit [python.org/downloads](https://www.python.org/downloads/windows/)
2. Download Python 3.9+ installer (64-bit recommended)
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH"
5. Click "Install Now"
6. Verify in Command Prompt:
   ```cmd
   python --version
   pip --version
   ```

#### Option 2: Using Microsoft Store

1. Open Microsoft Store
2. Search for "Python 3.11" (or latest)
3. Click "Get" to install
4. Verify installation

#### Option 3: Using Chocolatey

```powershell
# Install Chocolatey if not already installed
# Run PowerShell as Administrator
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Python
choco install python

# Verify
python --version
```

---

## Project Installation

### Step 1: Download the Repository

#### Option 1: Using Git (Recommended)

```bash
# Clone the repository
git clone https://github.com/TrentPierce/Ethereum-Address-Collider.git

# Navigate to directory
cd Ethereum-Address-Collider
```

#### Option 2: Download ZIP

1. Visit https://github.com/TrentPierce/Ethereum-Address-Collider
2. Click "Code" → "Download ZIP"
3. Extract the ZIP file
4. Open terminal/command prompt in extracted folder

### Step 2: Create Virtual Environment (Recommended)

Virtual environments isolate project dependencies.

#### Linux/macOS

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should change to show (venv)
```

#### Windows

```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Your prompt should change to show (venv)
```

### Step 3: Install Dependencies

```bash
# Install required packages
pip install -r requirements.txt

# Verify installation
pip list
```

You should see:
- `requests` (version 2.25.0 or higher)

---

## API Key Setup

### Step 1: Obtain Etherscan API Key

1. **Visit Etherscan**:
   - Go to [https://etherscan.io/apis](https://etherscan.io/apis)

2. **Create Account**:
   - Click "Register"
   - Fill in email and password
   - Verify email address

3. **Generate API Key**:
   - Log in to your account
   - Navigate to "API Keys" section
   - Click "Add" to create new API key
   - Give it a descriptive name (e.g., "EthCollider")
   - Copy the generated API key

### Step 2: Set Environment Variable

#### Linux/macOS

**Temporary (current session):**
```bash
export ETHERSCAN_API_KEY='YOUR_API_KEY_HERE'
```

**Permanent (recommended):**

For bash users:
```bash
echo 'export ETHERSCAN_API_KEY="YOUR_API_KEY_HERE"' >> ~/.bashrc
source ~/.bashrc
```

For zsh users:
```bash
echo 'export ETHERSCAN_API_KEY="YOUR_API_KEY_HERE"' >> ~/.zshrc
source ~/.zshrc
```

#### Windows

**Temporary (Command Prompt):**
```cmd
set ETHERSCAN_API_KEY=YOUR_API_KEY_HERE
```

**Temporary (PowerShell):**
```powershell
$env:ETHERSCAN_API_KEY='YOUR_API_KEY_HERE'
```

**Permanent (System Settings):**

1. Open Start Menu
2. Search "environment variables"
3. Click "Edit the system environment variables"
4. Click "Environment Variables..." button
5. Under "User variables", click "New..."
6. Variable name: `ETHERSCAN_API_KEY`
7. Variable value: Your API key
8. Click "OK" on all dialogs
9. **Restart your terminal/command prompt**

### Step 3: Verify API Key

```bash
# Linux/macOS
echo $ETHERSCAN_API_KEY

# Windows Command Prompt
echo %ETHERSCAN_API_KEY%

# Windows PowerShell
echo $env:ETHERSCAN_API_KEY
```

You should see your API key displayed (keep it secret!).

---

## Verification

### Test Python Installation

```bash
python3 --version
# Should output: Python 3.6.x or higher
```

### Test Dependencies

```bash
python3 -c "import requests; print(f'requests {requests.__version__} installed')"
# Should output: requests 2.x.x installed
```

### Test Environment Variable

```bash
python3 -c "import os; print('API key:', 'SET' if os.getenv('ETHERSCAN_API_KEY') else 'NOT SET')"
# Should output: API key: SET
```

### Run the Program

```bash
python3 EthCollider.py
```

**Expected output:**
```
======================================================================
Ethereum Collider developed by Trent Pierce (www.SkeeBomb.com)
======================================================================
...
Starting 8 worker processes...
Worker 0 started (PID: ...)
...
```

**Success!** If you see this, installation is complete.

Press `Ctrl+C` to stop the program.

---

## Troubleshooting

### Python Not Found

**Problem**: `python3: command not found` or `python: command not found`

**Solution**:
- Ensure Python is installed (see [Python Installation](#python-installation))
- On Windows, use `python` instead of `python3`
- Check if Python is in PATH

### Permission Denied

**Problem**: `Permission denied` when installing

**Solution Linux/macOS**:
```bash
# Use --user flag
pip3 install --user -r requirements.txt

# Or use sudo (not recommended for production)
sudo pip3 install -r requirements.txt
```

**Solution Windows**:
- Run Command Prompt as Administrator
- Or use `--user` flag

### Module Not Found

**Problem**: `ModuleNotFoundError: No module named 'requests'`

**Solution**:
```bash
# Reinstall dependencies
pip3 install -r requirements.txt

# Or install directly
pip3 install requests
```

### API Key Not Set

**Problem**: `ERROR: ETHERSCAN_API_KEY environment variable not set!`

**Solutions**:

1. **Check if set**:
   ```bash
   echo $ETHERSCAN_API_KEY  # Linux/macOS
   echo %ETHERSCAN_API_KEY%  # Windows CMD
   ```

2. **Set temporarily**:
   ```bash
   export ETHERSCAN_API_KEY='your_key'  # Linux/macOS
   set ETHERSCAN_API_KEY=your_key  # Windows
   ```

3. **Restart terminal** after setting permanently

### Import Errors on Windows

**Problem**: `ModuleNotFoundError` or `ImportError`

**Solution**:
```cmd
# Ensure you're using the right Python
where python
python --version

# Use absolute path if needed
C:\Python39\python.exe EthCollider.py
```

### SSL Certificate Errors

**Problem**: `SSL: CERTIFICATE_VERIFY_FAILED`

**Solution**:
```bash
# Install/update certifi
pip3 install --upgrade certifi

# macOS specific
/Applications/Python\ 3.x/Install\ Certificates.command
```

### Rate Limit Errors

**Problem**: API returns rate limit errors immediately

**Solution**:
- Ensure you're using your own API key
- Free tier: 5 requests/second, 100k/day
- Wait if daily limit reached
- Consider upgrading Etherscan plan

### Virtual Environment Issues

**Problem**: Dependencies not found in virtual environment

**Solution**:
```bash
# Deactivate and recreate
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Multiprocessing Errors on Windows

**Problem**: Errors when starting worker processes

**Solution**:
```python
# Add to top of EthCollider.py if needed
if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    # ... rest of code
```

---

## Advanced Setup

### Using Virtual Environments

#### Why Use Virtual Environments?

- Isolate project dependencies
- Avoid conflicts with system packages
- Easy to reproduce environment
- Clean uninstallation

#### Creating and Using

```bash
# Create
python3 -m venv venv

# Activate
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Work on project...

# Deactivate when done
deactivate
```

### Development Installation

For contributors and developers:

```bash
# Clone with development branch
git clone -b develop https://github.com/TrentPierce/Ethereum-Address-Collider.git

# Install in development mode
pip install -e .

# Install development dependencies (if available)
pip install -r requirements-dev.txt
```

### Docker Installation (Advanced)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV ETHERSCAN_API_KEY=""

CMD ["python", "EthCollider.py"]
```

Build and run:

```bash
# Build image
docker build -t eth-collider .

# Run container
docker run -e ETHERSCAN_API_KEY='your_key' eth-collider
```

### System Service Setup (Linux)

Run as a system service:

1. Create service file `/etc/systemd/system/ethcollider.service`:

```ini
[Unit]
Description=Ethereum Address Collider
After=network.target

[Service]
Type=simple
User=yourusername
WorkingDirectory=/path/to/Ethereum-Address-Collider
Environment="ETHERSCAN_API_KEY=your_key"
ExecStart=/usr/bin/python3 /path/to/EthCollider.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

2. Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable ethcollider
sudo systemctl start ethcollider
sudo systemctl status ethcollider
```

### Performance Tuning

#### Adjust Worker Count

Edit `EthCollider.py`:

```python
# Use fewer workers (reduce CPU usage)
num_processes = 2

# Use more workers (if you have more cores)
num_processes = 16
```

#### Adjust Rate Limiting

Edit `EthCollider.py` (be careful not to violate API terms):

```python
# Slower (0.5 seconds between calls)
time.sleep(0.5)

# Faster (only if you have paid API plan)
time.sleep(0.1)
```

---

## Platform-Specific Notes

### macOS Apple Silicon (M1/M2)

Works natively on ARM architecture:

```bash
# Check architecture
uname -m
# Should show: arm64

# Python should work natively
python3 --version
```

### Raspberry Pi

Tested on Raspberry Pi 3B+ and 4:

```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip

# May need additional packages
sudo apt install python3-dev

# Follow standard installation
pip3 install -r requirements.txt
```

### Windows Subsystem for Linux (WSL)

Follow Linux instructions:

```bash
# Update WSL
sudo apt update && sudo apt upgrade

# Install Python
sudo apt install python3 python3-pip

# Follow Linux installation steps
```

---

## Uninstallation

### Remove Application

```bash
# If using virtual environment
deactivate
cd ..
rm -rf Ethereum-Address-Collider

# If installed system-wide
pip3 uninstall -r requirements.txt
```

### Remove Environment Variable

**Linux/macOS**:
```bash
# Remove from .bashrc or .zshrc
nano ~/.bashrc  # or ~/.zshrc
# Delete the ETHERSCAN_API_KEY line
source ~/.bashrc
```

**Windows**:
1. Open "Environment Variables" settings
2. Find and delete `ETHERSCAN_API_KEY`
3. Click OK

---

## Getting Help

If you encounter issues not covered here:

1. **Check existing issues**: [GitHub Issues](https://github.com/TrentPierce/Ethereum-Address-Collider/issues)
2. **Create new issue**: Include:
   - Your OS and version
   - Python version (`python3 --version`)
   - Complete error message
   - Steps to reproduce
3. **Community support**: [GitHub Discussions](https://github.com/TrentPierce/Ethereum-Address-Collider/discussions)

---

## Next Steps

After successful installation:

1. **Read the README**: [README.md](README.md)
2. **Review security**: [SECURITY.md](SECURITY.md)
3. **Understand the code**: Review source files
4. **Learn the math**: See README's Mathematical Analysis section
5. **Contribute**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Installation complete! Happy learning! 🎓**
