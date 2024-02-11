import requests

def check_sensitive_data_exposure(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            sensitive_keywords = ['password', 'credit_card', 'ssn', 'social_security_number']  
            for keyword in sensitive_keywords:
                if keyword in response.text:
                    print(f"Potential sensitive data exposure found! Keyword: {keyword}")
                    break
            else:
                print("No sensitive data exposure found.")
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error occurred while accessing {url}: {e}")

# URL for sensitive data exposure check
url = 'https://example.com/admin_panel'
check_sensitive_data_exposure(url)
