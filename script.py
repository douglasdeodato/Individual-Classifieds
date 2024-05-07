import requests
from bs4 import BeautifulSoup
import json
from docx import Document

# Function to download webpage content and parse it
def parse_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract the data you need from the parsed HTML
        # For demonstration purposes, let's say we're extracting the titles of listings
        listings = [listing.text.strip() for listing in soup.select('.listing-title')]
        return listings
    else:
        print(f"Failed to fetch {url}")
        return []

# Function to save data to JSON file
def save_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Function to save data to Word document
def save_to_word(data, filename):
    doc = Document()
    for item in data:
        doc.add_paragraph(item)
    doc.save(filename)

# Main function to download content from pages 1 to 50
def main():
    base_url = "https://iahip.org/Individual-Classifieds?pg="
    all_listings = []

    for page_num in range(1, 51):
        url = base_url + str(page_num)
        print(f"Downloading page {page_num}...")
        listings = parse_page(url)
        all_listings.extend(listings)

    # Save data to JSON
    save_to_json(all_listings, 'listings.json')

    # Save data to Word document
    save_to_word(all_listings, 'listings.docx')

    print("Data downloaded and saved successfully.")

if __name__ == "__main__":
    main()
