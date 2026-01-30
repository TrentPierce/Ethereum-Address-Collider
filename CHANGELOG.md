# Changelog

All notable changes to the Ethereum Address Collider project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-01-30

### 🎉 Major Release - Python 3 Migration

This is a comprehensive update that modernizes the entire codebase for Python 3.6+ and adds significant improvements to functionality, security, and documentation.

### Added

#### New Features
- **True Multiprocessing Implementation**: Worker processes now run in parallel, utilizing all CPU cores
- **Environment Variable Configuration**: API keys are now stored securely in environment variables
- **Rate Limiting**: Added 0.2s delay between API calls (5 req/sec) to respect Etherscan limits
- **Comprehensive Error Handling**: Network requests now have retry logic and graceful failure
- **Progress Tracking**: Real-time display of addresses checked across all workers
- **Timestamped Output Files**: Found wallets saved with timestamps for better organization
- **Inter-Process Communication**: Uses managed queues for safe worker coordination

#### Documentation
- **Updated README.md**: Complete rewrite with installation instructions, usage examples, and security warnings
- **requirements.txt**: Added for easy dependency management
- **.env.example**: Template for API key configuration
- **CHANGELOG.md**: This file, documenting all changes
- **Enhanced .gitignore**: Excludes Python artifacts, environment files, and private keys
- **Educational Disclaimers**: Prominent warnings about the impracticality of finding collisions

### Changed

#### Python 3 Migration
- **Print Statements**: Converted all `print` statements to `print()` functions
- **xrange to range**: Replaced all `xrange()` calls with `range()`
- **input vs raw_input**: Changed `raw_input()` to `input()`
- **Long Integer Literals**: Removed `L` suffix from long integers (Python 3 auto-promotes)
- **String/Bytes Handling**: 
  - Replaced `.encode('hex')` with `.hex()`
  - Replaced `.decode('hex')` with `bytes.fromhex()`
  - Properly handle bytes vs strings throughout codebase
- **Exception Syntax**: Changed `raise Exception, "msg"` to `raise Exception("msg")`
- **pickle Import**: Added try/except for `cPickle` with fallback to `pickle`

#### Security Improvements
- **Removed Hardcoded API Key**: The exposed Etherscan API key `V7GSGSMWZ2CZH1B6MBXM84SZ1XG4DXDCW9` has been removed
- **Environment Variable Usage**: API key now loaded via `os.getenv('ETHERSCAN_API_KEY')`
- **Validation**: Added checks for missing API key with helpful error messages
- **Private Key Protection**: Updated .gitignore to prevent committing sensitive files

#### Code Quality
- **Function Documentation**: Added docstrings to all functions
- **Variable Naming**: Improved clarity in variable names
- **Code Organization**: Better structure with separated concerns
- **Error Messages**: More informative error messages for debugging

#### Multiprocessing
- **Fixed Implementation**: The multiprocessing pool is now actually used (was created but unused in v1.0)
- **Worker Functions**: Dedicated worker function for parallel address generation
- **Result Aggregation**: Safe inter-process communication using managed queues
- **Graceful Shutdown**: Proper process termination on exit or interrupt

### Fixed

#### Bugs
- **Unused Multiprocessing Pool**: The Pool object was created but never utilized - now properly implemented
- **Global Variable Issues**: Fixed confusing `balance` function that used global variable with same name
- **Indentation Errors**: Fixed mixed tabs/spaces causing Python errors
- **Import Issues**: Fixed relative imports in lib modules
- **Encoding Errors**: Fixed all bytes/string conversion issues for Python 3

#### Performance
- **Sequential Bottleneck**: Addresses are now generated in parallel instead of sequentially
- **API Call Efficiency**: Better handling of rate limits and retries

### Security

#### Vulnerabilities Fixed
- **CVE-NONE-HARDCODED-KEY**: Removed hardcoded API key from source code
- **Exposed Credentials**: API key no longer visible in public repository

#### Best Practices Implemented
- Environment variable usage for secrets
- .gitignore for sensitive files
- Template files (.env.example) for setup guidance
- Security disclaimers in documentation

### Technical Details

#### Files Modified
- `EthCollider.py`: Complete rewrite with Python 3 compatibility and multiprocessing
- `lib/ECDSA_BTC.py`: Python 3 migration, pickle compatibility
- `lib/python_sha3.py`: Fixed bytes/string handling for Python 3
- `README.md`: Comprehensive update with modern documentation
- `.gitignore`: Expanded to cover Python 3 artifacts and sensitive files

#### Files Added
- `requirements.txt`: Dependency specification
- `.env.example`: API key configuration template
- `CHANGELOG.md`: This changelog

#### Compatibility
- **Python Version**: Now requires Python 3.6+
- **Dependencies**: Only requires `requests` library
- **Operating Systems**: Windows, macOS, Linux (unchanged)

### Migration Guide

For users upgrading from v1.0:

1. **Install Python 3.6+** (if not already installed)
2. **Update dependencies**: `pip install -r requirements.txt`
3. **Set API key**: `export ETHERSCAN_API_KEY='your_key_here'`
4. **Run the updated script**: `python EthCollider.py`

### Performance Improvements

- **Multi-core Utilization**: Now uses all available CPU cores
- **Parallel Processing**: Multiple addresses checked simultaneously
- **Better Rate Management**: Respects API limits while maximizing throughput

### Known Issues

None at this time. Please report issues at: https://github.com/TrentPierce/Ethereum-Address-Collider/issues

---

## [1.0.0] - 2017-06-17

### Initial Release

- Python 2.7 implementation
- Single-threaded address generation
- Direct Etherscan API integration
- Pure Python ECDSA and SHA3 implementations
- Cross-platform support

---

## Legend

- 🎉 Major release
- ✨ New feature
- 🐛 Bug fix
- 🔒 Security fix
- 📝 Documentation
- ⚡ Performance improvement
- 💥 Breaking change
