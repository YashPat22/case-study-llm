import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from requests_html import HTMLSession

def scrape_and_save(url, output_file):
    session = HTMLSession()
    response = session.get(url)
    
    if response.status_code == 200:
        # Render JavaScript and wait for any dynamic content to load
        response.html.render()
        
        # Extract all text elements
        text_elements = response.html.find('body')[0].text
        
        # Save the text into a text file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text_elements)
            
        print(f"Text content saved to '{output_file}'")
    else:
        print("Failed to retrieve the web page.")

# Example usage
url = 'https://www.partselect.com/'
output_file = 'parts_select_text.txt'
scrape_and_save(url, output_file)
