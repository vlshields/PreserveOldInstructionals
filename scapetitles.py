# -*- coding: utf-8 -*-
"""
Spyder Editor

Copyright Vincent Shields
"""

import requests
from bs4 import BeautifulSoup
import os
from chapter1 import html_doc

"""Worm guard instructions came as .vob files in dvd format. 
The were converted to .mkv files with the powershell script 
included in the repo called "convertvobfiles.ps1"""

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser')
print(soup.prettify())

# [text for text in soup.stripped_strings]