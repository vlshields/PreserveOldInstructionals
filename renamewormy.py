import requests
from bs4 import BeautifulSoup
import os

"""Worm guard instructions came as .vob files in dvd format. 
The were converted to .mkv files with the powershell script 
included in the repo called "convertvobfiles.ps1"""

def get_chapter1Titles():
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

        # Find all span tags on the page
        span_tags = soup.find_all('span')

        # Add titles from span tags to a list
        titles = []
        for span_tag in span_tags:
            span_text = span_tag.text.strip()
            titles.append(str(span_text))
        return titles
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    print(titles.index('1-1 Introduction to the Lapel Encyclopedia'))

titles = get_chapter1Titles()
print(titles)


# def rename_titles(titles):

#         os.makedirs("Chapter 1")


