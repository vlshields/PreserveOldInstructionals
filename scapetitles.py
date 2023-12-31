# -*- coding: utf-8 -*-
"""
Spyder Editor

Copyright Vincent Shields
"""


from bs4 import BeautifulSoup
import os
from chapter1 import html_doc
from getfiles import get_files_list

"""Worm guard instructions came as .vob files in dvd format. 
The were converted to .mkv files with the powershell script 
included in the repo called "convertvobfiles.ps1"""


def get_chapter_1():
    
    soup = BeautifulSoup(html_doc,'html.parser')
    titles = [text for text in soup.stripped_strings]
    return titles

def make_chapter_1_folder(titles):
    os.makedirs("C:\\Users\\Vince\\Desktop\\WormGuard\\{titles[0]}")
    
def separate_duration_from_titles(titles):
    
    duration = list()
    titles.pop[0]
    for i in titles:
        if len(i) < 8:
            duration.append(i)
            del titles[i]
    return duration,titles

def add_chap_and_length(duration,titles,oldfiles):
    duration,titles = separate_duration_from_titles(titles)
    oldfiles = get_files_list()
    for title,duration,old in zip(titles,duration,oldfiles):
        os.rename(old, title + duration + '.mkv')
    
    
