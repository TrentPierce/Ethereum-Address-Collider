# Contributing to Ethereum Address Collider

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

---

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

### Our Values

- **Respect**: Treat everyone with respect and kindness
- **Education**: Focus on learning and teaching
- **Ethics**: Use technology responsibly
- **Collaboration**: Work together constructively
- **Openness**: Be transparent and honest

---

## How Can I Contribute?

### Reporting Bugs

**Before Submitting**:
1. Check [existing issues](https://github.com/TrentPierce/Ethereum-Address-Collider/issues)
2. Verify you're using the latest version
3. Try to reproduce the issue

**Bug Report Should Include**:
- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Error messages (full traceback)
- Screenshots (if applicable)

**Template**:
```markdown
## Bug Description
Brief description of the issue

## Steps to Reproduce
1. Go to...
2. Run command...
3. See error...

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: Ubuntu 22.04
- Python: 3.9.7
- Version: 2.0.0

## Error Output
```
paste error here
```

## Additional Context
Any other relevant information
```

### Suggesting Enhancements

**Before Suggesting**:
1. Check if it already exists
2. Consider if it fits the project scope
3. Think about implementation

**Enhancement Proposal Should Include**:
- Clear use case
- Benefits to users
- Implementation ideas
- Potential drawbacks
- Examples

### Improving Documentation

Documentation improvements are always welcome:
- Fix typos or unclear wording
- Add examples
- Improve explanations
- Translate to other languages
- Create tutorials or guides

### Writing Code

Areas where contributions are needed:
- Bug fixes
- Performance improvements
- New features (discuss first!)
- Test coverage
- Code refactoring

---

## Getting Started

### Prerequisites

- Python 3.6+
- Git
- GitHub account
- Basic understanding of:
  - Python programming
  - Git/GitHub workflow
  - Cryptography (helpful but not required)

### Fork and Clone

```bash
# Fork on GitHub (click "Fork" button)

# Clone your fork
git clone https://github.com/YOUR_USERNAME/Ethereum-Address-Collider.git
cd Ethereum-Address-Collider

# Add upstream remote
git remote add upstream https://github.com/TrentPierce/Ethereum-Address-Collider.git

# Verify remotes
git remote -v
```

### Set Up Development Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Install development tools (optional)
pip install pylint black pytest bandit

# Set up API key
export ETHERSCAN_API_KEY='your_test_key'

# Test installation
python3 EthCollider.py
```

---

## Development Workflow

### Branch Strategy

**Main Branches**:
- `master` - Stable, production-ready code
- `develop` - Integration branch for features (if exists)

**Feature Branches**:
- Create from `master` or `develop`
- Use descriptive names
- Delete after merge

**Naming Convention**:
```
feature/add-logging-system
fix/api-timeout-issue
docs/improve-readme
refactor/optimize-address-generation
test/add-unit-tests
```

### Typical Workflow

```bash
# 1. Update your fork
git checkout master
git fetch upstream
git merge upstream/master

# 2. Create feature branch
git checkout -b feature/your-feature-name

# 3. Make changes
# Edit files...

# 4. Test changes
python3 EthCollider.py
# Run any tests

# 5. Commit changes
git add .
git commit -m "Add feature: description"

# 6. Push to your fork
git push origin feature/your-feature-name

# 7. Create Pull Request on GitHub
```

### Commit Messages

**Format**:
```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples**:
```bash
# Good
git commit -m "feat: Add rate limiting for API calls"
git commit -m "fix: Handle JSON decode errors in API response"
git commit -m "docs: Update installation instructions for macOS"

# Bad
git commit -m "fixed stuff"
git commit -m "update"
git commit -m "changes"
```

**Detailed Commit**:
```bash
git commit -m "feat: Add worker restart on crash

Workers now automatically restart if they encounter
an unhandled exception. This improves reliability for
long-running sessions.

Closes #42"
```

---

## Coding Standards

### Python Style Guide

Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some flexibility.

**Use a Linter**:
```bash
# Install
pip install pylint

# Run
pylint EthCollider.py
pylint lib/*.py
```

**Or use Black** (auto-formatter):
```bash
# Install
pip install black

# Format
black EthCollider.py
black lib/
```

### Code Style

**Indentation**:
```python
# Use 4 spaces (not tabs)
def my_function():
    if condition:
        do_something()
```

**Naming Conventions**:
```python
# Functions and variables: snake_case
def calculate_address():
    private_key = generate_key()

# Classes: PascalCase
class AddressGenerator:
    pass

# Constants: UPPER_CASE
MAX_RETRIES = 3
API_TIMEOUT = 10
```

**Line Length**:
```python
# Max 100 characters (flexible to 120 for readability)

# Good
address = compute_adr(privkeynum)

# Acceptable (if more readable)
very_long_variable_name = some_function_with_many_parameters(
    param1, param2, param3, param4
)
```

**Imports**:
```python
# Order: stdlib, third-party, local
import os
import sys
import time

import requests

from lib.ECDSA_BTC import mulG, load_gtable
```

**Docstrings**:
```python
def check_balance(address, api_key):
    """Check balance of an Ethereum address using Etherscan API.
    
    Args:
        address (str): Ethereum address (40 hex characters)
        api_key (str): Etherscan API key
        
    Returns:
        str: Balance in Wei, or None if error
        
    Raises:
        requests.exceptions.RequestException: On network errors
        
    Example:
        >>> check_balance('0x742d35Cc6634C0532925a3b844Bc9e7595f0bEb0', 'key')
        '1000000000000000000'
    """
    # Implementation
```

**Type Hints** (encouraged):
```python
def generate_address(private_key: int) -> str:
    """Generate Ethereum address from private key."""
    pass

from typing import Optional, List

def worker_func(worker_id: int, queue: 'Queue') -> Optional[dict]:
    """Worker function for multiprocessing."""
    pass
```

### Code Quality

**Avoid**:
- Magic numbers (use constants)
- Deep nesting (max 4 levels)
- Long functions (max 50 lines ideally)
- Global variables (use parameters)
- Mutable default arguments

**Good Practices**:
```python
# Use constants
MAX_RETRIES = 3  # Not: retry 3 times

# Early returns
def validate_key(key):
    if not key:
        return False
    if len(key) != 64:
        return False
    return True

# Better than nested ifs

# Context managers
with open('file.txt', 'r') as f:
    data = f.read()
# File automatically closed

# List comprehensions (when clear)
squares = [x**2 for x in range(10)]

# Not:
squares = []
for x in range(10):
    squares.append(x**2)
```

---

## Testing Guidelines

### Running Tests

```bash
# If tests exist
python3 -m pytest

# With coverage
pip install pytest-cov
pytest --cov=. --cov-report=html
```

### Writing Tests

**Test File Structure**:
```
tests/
├── __init__.py
├── test_address_generation.py
├── test_multiprocessing.py
└── test_api_calls.py
```

**Example Test**:
```python
# tests/test_address_generation.py
import pytest
from EthCollider import compute_adr, hexa

def test_hexa_converts_to_64_chars():
    """Test hexa() pads to 64 characters."""
    result = hexa(255)
    assert len(result) == 64
    assert result.endswith('ff')

def test_compute_adr_returns_40_chars():
    """Test address generation returns 40 hex chars."""
    # Use known test key
    test_key = 1
    address = compute_adr(test_key)
    assert len(address) == 40
    assert all(c in '0123456789abcdef' for c in address)

@pytest.mark.skipif(
    not os.getenv('ETHERSCAN_API_KEY'),
    reason="API key not set"
)
def test_check_balance_with_real_api():
    """Test API call with real key."""
    # Test with known address
    pass
```

### Manual Testing

**Before Submitting PR**:
1. Run the program: `python3 EthCollider.py`
2. Verify no errors
3. Test Ctrl+C graceful shutdown
4. Check all new features work
5. Test on target Python versions

---

## Documentation

### Code Documentation

**Every function should have**:
- Brief description
- Parameters explained
- Return value described
- Example (if complex)
- Exceptions listed

**Example**:
```python
def randomforkey():
    """Generate a random private key within valid range.
    
    Uses cryptographically secure randomness (os.urandom) to
    generate a 256-bit private key that falls within the valid
    range for the secp256k1 elliptic curve.
    
    Returns:
        int: Random integer in range [1, secp256k1_order)
        
    Note:
        May loop multiple times if random number falls outside
        valid range (extremely rare).
        
    Example:
        >>> key = randomforkey()
        >>> 1 <= key < 0xFFFFF...  # Valid range
        True
    """
```

### Documentation Files

**Update when changing**:
- README.md - For user-facing changes
- CHANGELOG.md - For all changes
- INSTALL.md - For setup changes
- SECURITY.md - For security changes

### Inline Comments

**When to comment**:
- Complex algorithms
- Non-obvious code
- Mathematical formulas
- Workarounds
- Security considerations

**Example**:
```python
# Use secp256k1 curve order to ensure valid private key
# Order: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

while candint < 1 or candint >= r:
    # Generate 1024 random bytes and hash to get uniform distribution
    cand = hashrand(1024)
    candint = int(cand, 16)
    # Probability of rejection: ~2^-1024 (negligible)
```

---

## Pull Request Process

### Before Submitting

**Checklist**:
- [ ] Code follows style guidelines
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] Branch is up to date with master
- [ ] No merge conflicts
- [ ] Changes are focused (one feature/fix per PR)

### Creating Pull Request

1. **Push to your fork**:
   ```bash
   git push origin feature/your-feature
   ```

2. **Go to GitHub** and click "New Pull Request"

3. **Fill out template**:
   ```markdown
   ## Description
   Brief description of changes
   
   ## Motivation
   Why is this change needed?
   
   ## Changes Made
   - Added feature X
   - Fixed bug Y
   - Updated docs Z
   
   ## Testing
   How was this tested?
   
   ## Checklist
   - [x] Code follows style guide
   - [x] Tests pass
   - [x] Documentation updated
   
   ## Screenshots (if applicable)
   ![screenshot](url)
   ```

4. **Request review** from maintainers

### Review Process

**What happens**:
1. Automated checks run (if configured)
2. Maintainer reviews code
3. Feedback provided
4. You make requested changes
5. Re-review
6. Approval and merge

**Timeline**:
- Initial review: Within 1 week
- Follow-up: 2-3 days per iteration

**Be patient and respectful** during reviews!

### After Merge

```bash
# Update your local repository
git checkout master
git fetch upstream
git merge upstream/master

# Delete feature branch
git branch -d feature/your-feature
git push origin --delete feature/your-feature
```

---

## Community

### Getting Help

- **Questions**: [GitHub Discussions](https://github.com/TrentPierce/Ethereum-Address-Collider/discussions)
- **Issues**: [GitHub Issues](https://github.com/TrentPierce/Ethereum-Address-Collider/issues)
- **Email**: Pierce.trent@gmail.com

### Communication

**Be**:
- Respectful and kind
- Clear and concise
- Patient with responses
- Constructive in feedback

**Avoid**:
- Demanding or entitled tone
- Personal attacks
- Off-topic discussions
- Spamming

### Recognition

Contributors will be:
- Listed in CHANGELOG.md
- Mentioned in release notes
- Credited in README (for significant contributions)

---

## Development Resources

### Learning Resources

**Python**:
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)

**Cryptography**:
- [Practical Cryptography for Developers](https://cryptobook.nakov.com/)
- [Ethereum Yellow Paper](https://ethereum.github.io/yellowpaper/paper.pdf)

**Git/GitHub**:
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [GitHub Guides](https://guides.github.com/)

### Tools

**Recommended**:
- **Editor**: VS Code, PyCharm, Sublime Text
- **Linter**: pylint, flake8
- **Formatter**: black
- **Git GUI**: GitKraken, GitHub Desktop
- **API Testing**: Postman, curl

---

## Questions?

Don't hesitate to ask questions! We're here to help.

- Open a [Discussion](https://github.com/TrentPierce/Ethereum-Address-Collider/discussions)
- Create an [Issue](https://github.com/TrentPierce/Ethereum-Address-Collider/issues)
- Email: Pierce.trent@gmail.com

---

**Thank you for contributing! 🎉**

Every contribution, no matter how small, helps improve this educational tool and benefits the entire community.
