import requests
from bs4 import BeautifulSoup
import fire

def crawl_site(url):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(crawl_site)

# URL of the API documentation website
url = "https://api.example.com/docs/"

# Send a request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the overview section
overview_section = soup.find("div", {"id": "overview"})
if overview_section:
    overview_content = overview_section.get_text(strip=True)
    print("Overview:")
    print(overview_content)

# Extract the endpoints section
endpoints_section = soup.find("div", {"id": "endpoints"})
if endpoints_section:
    endpoints_content = endpoints_section.get_text(strip=True)
    print("\nEndpoints:")
    print(endpoints_content)

# Extract the authentication section
auth_section = soup.find("div", {"id": "authentication"})
if auth_section:
    auth_content = auth_section.get_text(strip=True)
    print("\nAuthentication:")
    print(auth_content)
