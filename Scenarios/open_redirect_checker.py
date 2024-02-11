import requests

def check_open_redirect_vulnerability(url, redirect_url):
    try:
        params = {'redirect': redirect_url}
        response = requests.get(url, params=params, allow_redirects=False)

        if response.status_code == 302 and redirect_url in response.headers['Location']:
            print("Potential Open Redirect vulnerability found!")
        else:
            print("No Open Redirect vulnerability found.")
    except requests.RequestException as e:
        print(f"Error occurred while accessing {url}: {e}")

url = 'https://example.com/redirect'
redirect_url = 'https://malicious-site.com'
check_open_redirect_vulnerability(url, redirect_url)
