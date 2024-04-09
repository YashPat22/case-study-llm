import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_links_from_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [urljoin(url, link.get('href')) for link in soup.find_all('a', href=True)]
        return links
    else:
        return []

def extract_text_from_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        text_elements = soup.find_all(text=True)
        page_text = '\n'.join(element.strip() for element in text_elements if element.strip())
        return page_text
    else:
        return ''

def scrape_website(url, output_file):
    visited = set()
    queue = [url]

    with open(output_file, 'w', encoding='utf-8') as f:
        while queue:
            current_url = queue.pop(0)
            if current_url not in visited:
                visited.add(current_url)
                print("Scraping:", current_url)

                # Extract text from current page
                page_text = extract_text_from_page(current_url)
                f.write(page_text + '\n')

                # Get links from current page
                links = get_links_from_page(current_url)
                for link in links:
                    if link not in visited:
                        queue.append(link)

# Usage
url = 'https://www.partselect.com/'
output_file = 'parts_select_text.txt'
scrape_website(url, output_file)
