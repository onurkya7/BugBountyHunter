# BugBountyHunter

This repository contains a set of tools written to check various web application security vulnerabilities.

<img src="https://img.shields.io/badge/Used Python 3.9.13- red">

<img src="https://img.shields.io/badge/Licence-MIT-yellowgreen">

## Setup Environment

```bash
# Make sure your PIP is up to date
pip install -U pip wheel setuptools

# Install required dependencies
pip install -r requirements.txt
```

## Tools

### Authentication Bypass Checker
- This tool is used to detect authentication bypass vulnerabilities.

### Command Injection Checker
- This tool checks for command injection vulnerabilities with basic scenarios.

### Directory Traversal Checker
- This tool checks for directory traversal vulnerabilities with basic scenarios.

### Open Redirect Checker
- This tool checks for open redirect vulnerabilities with basic scenarios.

### Prototype Pollution Checker
- This tool checks for prototype pollution and XXE (XML External Entity) vulnerabilities.

### Sensitive Data Checker
- This tool checks for sensitive data leakage vulnerabilities with basic scenarios.

### SSRF (Server-Side Request Forgery) Checker
- This tool checks for authentication bypass, SSTI (Server-Side Template Injection), and SSRF vulnerabilities.

### SSTI (Server-Side Template Injection) Checker
- This tool checks for authentication bypass, SSTI, and SSRF vulnerabilities.

### XXE (XML External Entity) Vulnerability Checker
- This tool checks for prototype pollution and XXE vulnerabilities.
  

## License

Our project is licensed under the [MIT License](LICENSE).

