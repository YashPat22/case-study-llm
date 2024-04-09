import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the text elements in the HTML
        text_elements = soup.find_all(text=True)
        
        # Filter out unwanted elements (e.g., script and style tags)
        filtered_text = [element.strip() for element in text_elements if element.parent.name not in ['script', 'style']]
        
        # Join the filtered text elements into a single string
        extracted_text = ' '.join(filtered_text)
        
        return extracted_text
    else:
        print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
        return None

# Example usage
url = 'https://www.partselect.com/Dishwasher-Parts.htm'
extracted_text = extract_text_from_url(url)
if extracted_text:
    print(extracted_text)