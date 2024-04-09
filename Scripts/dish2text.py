from bs4 import BeautifulSoup

# Open the HTML file
with open('/Users/yashpatawari/case-study-llm/dishwash.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract text
text = soup.get_text()

# Save the extracted text to a text file
with open('extracted_text_dishwash.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)
