import requests
from bs4 import BeautifulSoup
import urllib.parse
def google_search(query, num_results=10):
    base_url = "https://www.google.com/search"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
    }
    params = {
        "q": query,
        "num": num_results
    }

    # Sends a GET request to Google’s search URL with the specified headers and params. The response (HTML content) is stored in the response variable.
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        print("Failed to retrieve results")
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for result in soup.select('.tF2Cxc'):
        title_element = result.select_one('h3')
        link_element = result.select_one('a')
        description_element = result.select_one('.VwiC3b')

        # Check if all elements are present
        if title_element and link_element and description_element:
            results.append({
                "title": title_element.get_text(),
                "link": link_element['href'],
                "description": description_element.get_text()
            })

    # if results are empty
    if not results:
        print("No results found. The HTML structure might have changed.")
    
    return results

# Usage
query = "HTML tutorial"
results = google_search(query, num_results=10)

for idx, result in enumerate(results, start=1):
    print(f"{idx}. {result['title']}")
    print(f"   Link: {result['link']}")
    print(f"   Description: {result['description']}\n")