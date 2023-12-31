# -*- coding: utf-8 -*-
"""
Spyder Editor

Copyright Vincent Shields
"""

import requests
from bs4 import BeautifulSoup
import os
from chapter1 import html_doc
from getfiles import get_files_list

"""Worm guard instructions came as .vob files in dvd format. 
The were converted to .mkv files with the powershell script 
included in the repo called "convertvobfiles.ps1"""

import requests
from bs4 import BeautifulSoup

def get_chapter_1():
    soup = BeautifulSoup(html_doc,'html.parser')

    
    titles = [text for text in soup.stripped_strings]
    return titles

def make_chapter_1_folder(titles):
    os.makedirs("C:\\Users\\Vince\\Desktop\\WormGuard\\{titles[0]}")
    
def add_titles_with_duration(titles):
    torename = get_files_list()
    duration = list()
    for i in titles:
        if len(i) < 8:
            duration.append(i)
            del titles[i]
    return duration,titles
    
