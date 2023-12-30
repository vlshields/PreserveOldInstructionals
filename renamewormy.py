import os

import requests
from bs4 import BeautifulSoup

def get_dvd1_names():
	
	url = "https://jiujitsux.com/courses/keenans-lapel-encyclopedia/"
	# Set headers to simulate a web browser request
	headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
				}
	# Send a GET request to the URL
	response = requests.get(url,headers=headers)

	# Check if the request was successful (status code 200)
	if response.status_code == 200:
	    # Parse the HTML content of the page
	    soup = BeautifulSoup(response.content, 'html.parser')

	    # Find the h4 element with class 'tutor-course-content-list'
	    h4_element = soup.find('h4', class_='tutor-course-content-list')

	    if h4_element:
	        # Extract the text from the h4 element
	        h4_text = h4_element.text.strip()
	        print(f"Content from h4 element: {h4_text}")

	        # Find the ul element under the div with class 'tutor-course-content-list'
	        ul_element = h4_element.find_next('ul')

	        if ul_element:
	            # Extract the text from the ul element
	            ul_text = ul_element.text.strip()
	            print(f"Content from ul element: {ul_text}")
	        else:
	            print("No ul element found.")
	    else:
	        print("No h4 element with class 'tutor-course-content-list' found.")
	else:
	    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
get_dvd1_names()
# def rename_chapter1(newname):
	
# 	# Specify the current and new folder names
# 	current_folder_path = '/path/to/your/current/folder'
# 	new_folder_name = newname

# 	# Construct the new folder path
# 	new_folder_path = os.path.join(os.path.dirname(current_folder_path), new_folder_name)

# 	# Rename the folder
# 	try:
# 	    os.rename(current_folder_path, new_folder_path)
# 	    print(f"Folder renamed successfully. New folder path: {new_folder_path}")
# 	except OSError as e:
# 	    print(f"Error: {e}")