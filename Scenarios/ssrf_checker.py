import requests
from urllib.parse import urlparse

# List of allowed URLs
ALLOWED_DOMAINS = ['example.com', 'internal-site.local']

def is_internal_url(url):
    parsed_url = urlparse(url)
    domain = parsed_url.hostname
    if domain and any(domain.endswith(allowed) for allowed in ALLOWED_DOMAINS):
        return True
    return False

def check_ssrf_vulnerability(url):
    try:
        internal_url = 'http://internal-site.local/secret'
        
        if not is_internal_url(internal_url):
            print("Invalid internal URL provided. Potential SSRF attempt detected.")
            return
        
        response = requests.get(url, params={'url': internal_url}, timeout=5)
        response.raise_for_status()
        
        if 'Internal Site Secret' in response.text:
            print("Potential SSRF vulnerability found!")
            print("Response content:", response.text)
        else:
            print("No SSRF vulnerability found.")
        
        if response.status_code in [301, 302, 303, 307, 308]:
            print("Server returned a redirect status code which might indicate SSRF vulnerability:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# URL for SSRF check
url = 'https://example.com/external_api'
check_ssrf_vulnerability(url)
