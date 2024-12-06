# Web Scraping to Identify Forms and Input Fields
import requests
from bs4 import BeautifulSoup

def scrape_forms(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch page")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    forms = soup.find_all('form')
    form_details = []

    for form in forms:
        form_action = form.get('action')
        form_method = form.get('method')
        inputs = form.find_all('input')
        input_names = [input_tag.get('name') for input_tag in inputs if input_tag.get('name')]

        form_details.append({
            "action": form_action,
            "method": form_method,
            "input_fields": input_names
        })

    return form_details

# SQL Injection Test (Using SQLMap API)
import subprocess

def test_sql_injection(url, param):
    # Using subprocess to run sqlmap in a shell
    command = f"sqlmap -u {url} --data=\"{param}=1\" --batch --level=5 --risk=3 --dump"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if "sqlmap identified the following injection points" in str(stdout):
        return True, stdout.decode('utf-8')
    return False, "No SQL injection vulnerability found."

# XSS Testing
import requests

def test_xss(url, param):
    payload = "<script>alert('XSS')</script>"
    data = {param: payload}
    response = requests.post(url, data=data)

    if payload in response.text:
        return True, f"XSS vulnerability detected at {url} with payload {payload}"
    return False, "No XSS vulnerability detected."


# Security Headers Check
def check_security_headers(url):
    response = requests.get(url)
    headers = response.headers

    missing_headers = []
    required_headers = [
        "Strict-Transport-Security",
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Content-Security-Policy"
    ]

    for header in required_headers:
        if header not in headers:
            missing_headers.append(header)

    return missing_headers
