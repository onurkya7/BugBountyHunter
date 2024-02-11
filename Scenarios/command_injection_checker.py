import requests

def check_command_injection_vulnerability(url):
    try:
        payload = '; ls -la /'
        response = requests.post(url, data={'search': payload}, timeout=5)  # Timeout added to the request

        if response.status_code == 200 and 'index.html' in response.text:
            print("Potential Command Injection vulnerability found!")
            
        else:
            print("No Command Injection vulnerability found.")
    except requests.RequestException as e:
        print(f"Error occurred while accessing {url}: {e}")

# URL for Command Injection vulnerability check
url = 'https://example.com/search'
check_command_injection_vulnerability(url)
