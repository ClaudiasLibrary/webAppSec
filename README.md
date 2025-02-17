# Web Application Security Auditing Tool

## Theory behind the code
[Web Applications Vulnerabilities](https://claudiaslibrary.notion.site/Web-Applications-Vulnerabilities-12b19f756832801f9e2dd32a86bd628b)

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
Clone this repository and install the required dependencies

## Example Output of Security Audit Script

```bash
Starting security audit for https://example.com...
Scraping forms and input fields...
Testing for SQL Injection vulnerability on parameter: username...
SQL Injection vulnerability detected on username. Result: Vulnerable to SQL Injection.
Testing for SQL Injection vulnerability on parameter: password...
No SQL Injection vulnerability detected on password.
Testing for XSS vulnerability on parameter: username...
XSS vulnerability detected on username. Result: Cross-site scripting found.
Testing for XSS vulnerability on parameter: password...
No XSS vulnerability detected on password.
Checking for missing security headers...
Security audit completed. Report generated: security_report.html
```


### Generated Report (HTML)

```html
<html>
<head><title>Security Scan Report</title></head>
<body>
    <h1>Security Scan Report</h1>
    <h2>Vulnerabilities Detected</h2>
    <p>SQL Injection vulnerability detected on username. Result: Vulnerable to SQL Injection.</p>
    <p>XSS vulnerability detected on username. Result: Cross-site scripting found.</p>
    <p>Missing security headers: X-Frame-Options, Strict-Transport-Security</p>
</body>
</html>
```


### Explanation

1. **Input**: The script starts by running a security audit on a target URL (`https://example.com`).
2. **Form Scraping**: The script scrapes all forms and input fields from the target URL.
3. **SQL Injection Test**: It checks each form parameter for SQL Injection vulnerabilities.
   - In this example, the parameter `username` is found to be vulnerable to SQL Injection, but `password` is safe.
4. **XSS Test**: The script tests each form parameter for XSS (Cross-Site Scripting) vulnerabilities.
   - The `username` field is found to be vulnerable to XSS, while `password` is safe.
5. **Security Header Check**: The script checks for missing security headers (like `X-Frame-Options`, `Strict-Transport-Security`).
   - Missing headers are added to the report if detected.
6. **Report Generation**: After completing the audit, the results are saved to an HTML report, which details all detected vulnerabilities.
7. **Output**: The script generates a report in the file `security_report.html`.
