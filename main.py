from config import TARGET_URL, OUTPUT_REPORT
from utils import scrape_forms, test_sql_injection, test_xss, check_security_headers


def generate_report(vulnerabilities):
    with open(OUTPUT_REPORT, 'w') as file:
        file.write("<html><head><title>Security Scan Report</title></head><body>")
        file.write("<h1>Security Scan Report</h1>")
        file.write("<h2>Vulnerabilities Detected</h2>")
        for vuln in vulnerabilities:
            file.write(f"<p>{vuln}</p>")
        file.write("</body></html>")


def run_security_audit():
    print(f"Starting security audit for {TARGET_URL}...")

    # Scraping forms
    print("Scraping forms and input fields...")
    forms = scrape_forms(TARGET_URL)
    vulnerabilities = []

    # Check for SQL injection vulnerabilities
    for form in forms:
        for param in form["input_fields"]:
            print(f"Testing for SQL Injection vulnerability on parameter: {param}...")
            vuln, result = test_sql_injection(TARGET_URL, param)
            if vuln:
                vulnerabilities.append(f"SQL Injection vulnerability detected on {param}. Result: {result}")

    # Check for XSS vulnerabilities
    for form in forms:
        for param in form["input_fields"]:
            print(f"Testing for XSS vulnerability on parameter: {param}...")
            vuln, result = test_xss(TARGET_URL, param)
            if vuln:
                vulnerabilities.append(f"XSS vulnerability detected on {param}. Result: {result}")

    # Check for security headers
    print("Checking for missing security headers...")
    missing_headers = check_security_headers(TARGET_URL)
    if missing_headers:
        vulnerabilities.append(f"Missing security headers: {', '.join(missing_headers)}")

    # Generate report
    generate_report(vulnerabilities)
    print(f"Security audit completed. Report generated: {OUTPUT_REPORT}")


if __name__ == "__main__":
    run_security_audit()
