import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    print("Response status code:", response.status_code)
    
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all elements within the <div> tag with class 'part-section'
        sections = soup.find_all('div', class_='part-section')
        
        # Open a text file to write the scraped content
        with open('scraped_content.txt', 'w', encoding='utf-8') as f:
            for section in sections:
                # Find all elements with class 'part-item'
                items = section.find_all(class_='part-item')
                for item in items:
                    # Write the text content of each item to the file
                    item_text = item.get_text(strip=True)
                    if item_text:
                        f.write(item_text)
                        f.write('\n\n')  # Add a new line between items
        
        print("Scraping and saving completed successfully!")
    
    else:
        print("Failed to retrieve the webpage")

# URL of the website to scrape
url = 'https://www.partselect.com/Dishwasher-Parts.htm'

# Call the function to scrape the website
scrape_website(url)
