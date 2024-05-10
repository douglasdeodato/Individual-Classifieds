import requests
import json
from bs4 import BeautifulSoup

# Read URL from the JSON file
with open("urls.json", "r") as f:
    data = json.load(f)
    base_url = data["url"]

# Dictionary to store IDs for each page
ids_per_page = {}

# Iterate through pages 1 to 50
for page_num in range(1, 51):
    # Construct the URL for the current page
    url = f"{base_url}&pg={page_num}"
    
    # Print description of the current URL
    print(f"Scraping {url}")

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the div element with class "blogPostListContainer"
    container = soup.find("div", class_="blogPostListContainer")

    # Find the ul element with class "boxesList" inside the container
    ul_element = container.find("ul", class_="boxesList")

    # Find all li elements with class "boxesListItem" inside the ul_element
    li_elements = ul_element.find_all("li", class_="boxesListItem")

    # List to store IDs for the current page
    page_ids = []

    # Get the IDs of each li element and add them to the list
    for li in li_elements:
        li_id = li.get("id")
        if li_id:
            page_ids.append(li_id)

    # Store IDs for the current page in the dictionary
    ids_per_page[f"page_{page_num}"] = page_ids

# Save IDs for each page to a JSON file
with open("ids_per_page.json", "w") as f:
    json.dump(ids_per_page, f, indent=4)

print("IDs per page saved to ids_per_page.json")
