import requests
from bs4 import BeautifulSoup

def check_authentication_bypass_vulnerability(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP error status
        
        soup = BeautifulSoup(response.text, 'html.parser')
        admin_links = soup.find_all('a', href=True, text='Admin Panel')  # Find admin panel links
        if admin_links:
            print("Potential Authentication Bypass vulnerability found! Admin panel links:", admin_links)
        else:
            print("No Authentication Bypass vulnerability found.")
        
        headers = response.headers
        for header in headers:
            if 'admin' in headers[header].lower():
                print("Found 'admin' expression in HTTP headers:", header, ":", headers[header])
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

# URL for Authentication Bypass check
url = 'https://example.com'
check_authentication_bypass_vulnerability(url)
