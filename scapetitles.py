# -*- coding: utf-8 -*-
"""
Spyder Editor

Copyright Vincent Shields
"""

import requests
from bs4 import BeautifulSoup
import os

"""Worm guard instructions came as .vob files in dvd format. 
The were converted to .mkv files with the powershell script 
included in the repo called "convertvobfiles.ps1"""

import requests
from bs4 import BeautifulSoup

url = "https://jiujitsux.com/courses/keenans-lapel-encyclopedia/"

# Set headers to simulate a web browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

# Send a GET request with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all elements and extract the text
    all_text = soup.get_text(separator='\n', strip=True)
    titles = []
    for lines in all_text:
        titles.append(lines)

    # Print the extracted text
    text_file_path = 'output1.txt'
# Write the extracted text to a text file
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(all_text)

    print(f"Text written to {text_file_path}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")