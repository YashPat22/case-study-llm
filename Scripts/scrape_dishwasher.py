import requests
from bs4 import BeautifulSoup
import time

# URL of the website to scrape
url = "https://www.partselect.com/Dishwasher-Parts.htm"

# Make a request to the website
response = requests.get(url)
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
# Find all the "See more" buttons
see_more_buttons = soup.find_all("a", {"class": "see-more"})
# Initialize an empty list to store the data
data = []
# Scrape the data from the website, including the "See more" content
for button in see_more_buttons:
    # Click the "See more" button
    button.click()
    
    # Wait for the page to update
    time.sleep(2)
    
    # Parse the updated HTML content
    updated_response = requests.get(url)
    updated_soup = BeautifulSoup(updated_response.content, "html.parser")
    
    # Extract the relevant data from the page
    part_names = updated_soup.find_all("h3", {"class": "part-name"})
    part_descriptions = updated_soup.find_all("div", {"class": "part-description"})
    
    # Add the data to the list
    for name, description in zip(part_names, part_descriptions):
        data.append({
            "part_name": name.text.strip(),
            "part_description": description.text.strip()
        })
# Save the data to a text file
with open("dishwasher_parts.txt", "w", encoding="utf-8") as file:
    for item in data:
        file.write(f"Part Name: {item['part_name']}\n")
        file.write(f"Part Description: {item['part_description']}\n")
        file.write("\n")
print("Data saved to dishwasher_parts.txt")