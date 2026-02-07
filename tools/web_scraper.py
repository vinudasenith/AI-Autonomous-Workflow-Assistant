import requests
from bs4 import BeautifulSoup

def fetch_web_text(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs])
        return text
    except Exception as e:
        return f"Error fetching URL: {e}"

def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        return response.json()
    except Exception as e:
        return f"Error fetching API: {e}"
