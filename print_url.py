import os
import json
import requests
import time

# Create a folder to store HTML files
if not os.path.exists("html_files"):
    os.makedirs("html_files")

# Read IDs per page from the JSON file
with open("ids_per_page.json", "r") as f:
    ids_per_page = json.load(f)

# Iterate through each page
for page, ids in ids_per_page.items():
    # Create a folder for the current page
    page_folder = os.path.join("html_files", page)
    if not os.path.exists(page_folder):
        os.makedirs(page_folder)

    # Iterate through each ID on the page
    for li_id in ids:
        # Construct the URL for the current ID
        url = f"https://iahip.org/Individual-Classifieds/{li_id}"

        # Print description of the current URL
        print(f"Downloading {url}")

        # Send a GET request to the URL
        response = requests.get(url)

        # Save HTML content to a file
        file_path = os.path.join(page_folder, f"{li_id}.html")
        with open(file_path, "wb") as html_file:
            html_file.write(response.content)

        print(f"HTML content saved to {file_path}")

    # Introduce a 5-second delay before downloading the next page
    time.sleep(5)
