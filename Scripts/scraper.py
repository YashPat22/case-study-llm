import requests
from bs4 import BeautifulSoup

def scrape_and_save(url, output_file):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all text elements
        text_elements = soup.find_all(text=True)
        
        # Extract text from each element and concatenate
        page_text = '\n'.join(element.strip() for element in text_elements if element.strip())
        
        # Save the text into a text file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(page_text)
            
        print(f"Text content saved to '{output_file}'")
    else:
        print("Failed to retrieve the web page.")

# Usage
dishwasher_url = 'https://www.partselect.com/Dishwasher-Parts.htm'
fridge_url = 'https://www.partselect.com/Refrigerator-Parts.htm'
dish_output_file = 'dish_webpage_text.txt'
fridge_output_file = 'fridge_webpage_text.txt'
scrape_and_save(fridge_url, fridge_output_file)
scrape_and_save(dishwasher_url, dish_output_file)
