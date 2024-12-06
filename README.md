# Web Application Security Auditing Tool

## Overview
This tool automates the process of auditing a web application for common security vulnerabilities
such as SQL Injection, Cross-Site Scripting (XSS), and missing HTTP security headers.
The results of the audit are stored in an HTML report for easy review.

## Features
- Automatically scrape all forms and input fields.
- Test for SQL Injection vulnerabilities using SQLMap.
- Test for XSS vulnerabilities by injecting payloads.
- Check for missing HTTP security headers (like `Strict-Transport-Security`, `X-Content-Type-Options`, etc.).

## Requirements
- Python 3.x
- `requests`, `beautifulsoup4`, `sqlmap` (installed via `pip`)

## Installation
Clone this repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/web_app_security_audit_tool.git
cd web_app_security_audit_tool
pip install -r requirements.txt
```
