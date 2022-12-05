import requests
from bs4 import BeautifulSoup

# URL of the web page you want to extract text from
url = "https://en.wikipedia.org/wiki/Natural_language_processing"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# Extract all the text from the page
text = soup.get_text()

# Save the text to a file
with open("text.txt", "w") as file:
    file.write(text)
