import requests
from bs4 import BeautifulSoup

def get_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return None

def search_keywords(content, keywords):
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text().lower()
    found_keywords = {kw: text.count(kw.lower()) for kw in keywords}
    return found_keywords

def main():
    url = input("Enter the website URL (including https:// or http://): ")
    keywords = input("Enter keywords to search (comma-separated): ").split(',')
    
    content = get_website_content(url)
    if content:
        results = search_keywords(content, keywords)
        print("Keyword occurrences:")
        for keyword, count in results.items():
            print(f"{keyword.strip()}: {count}")

if __name__ == "__main__":
    main()
