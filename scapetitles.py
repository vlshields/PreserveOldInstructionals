# -*- coding: utf-8 -*-
"""
Spyder Editor

Copyright Vincent Shields
"""


from bs4 import BeautifulSoup
import os
from chapters import *
from glob import glob


"""Worm guard instructions came as .vob files in dvd format. 
The were converted to .mkv files with the powershell script 
included in the repo called "convertvobfiles.ps1"""

class ScrapeLapelGuard:
    
    def __init__(self,chapter,html):
        
        # Name the chapter of the disk, this will become the folder name
        self.chapter = chapter
        # provide html that contains the text data of a given disk
        # have provided them in chapters.py
        self.html = html
        
    def get_titles(self):
        
        """Get the names of the course sections for a given disk"""
        
        soup = BeautifulSoup(self.html,'html.parser')
        # We don't need the name of the chapter
        titles = [text for text in soup.stripped_strings if "Chapter" not in text]
        
        # Separate the section titles from the time durations
        titles = [i for i in titles if len(i)>6]
        
        # Replace ACSII characters that are not allowed in in windows os
        # as directory names. This will need to be adjusted/expanded based
        # on the OS you are using
        titles = [i.replace("50/50","FiftyFifty") for i in titles]
        titles = [i.replace(":"," -") for i in titles]
        titles = [i.replace("*","i") for i in titles]
    
        return titles

    def make_chapter_folder(self):
        
        """Add a new folder for a given disk, this is optional"""
        
        new_folder_path = "C:\\Users\\Vince\\Desktop\\WormGuard\\"+self.chapter
        
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        
        return new_folder_path
    
    def get_duration(self):
        
        """Get the duration of each section. This is also optional. Scrolling
        over the file with your mouse should also give you the video duration"""
        
        soup = BeautifulSoup(self.html,'html.parser')
        titles = [text for text in soup.stripped_strings if "Chapter" not in text]
        
        # Windows does not allow colons in directory names
        duration = [i.replace(':', '-') for i in titles if len(i) < 6]
        
        return duration

    def getfiles(self,filepath):
        return list(glob(filepath))
"""    
if __name__=='__main__':
    
    disk2 = ScrapeLapelGuard("chapter2", chapter2)
    titles = disk2.get_titles()
    duration = disk2.get_duration()
    folder = disk2.make_chapter_folder()
    
    old = getfiles("C:\\Users\\Vince\\Desktop\\WormGuard\\*.mkv")
    
    for oldfile,newfile,time in zip(old,titles,duration):
        time = time.replace(':', '-')
        os.rename(oldfile,folder+'\\'+str(newfile)+"_"+str(time)+".mkv")
"""