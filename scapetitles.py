# -*- coding: utf-8 -*-
"""
Spyder Editor

Copyright Vincent Shields
"""


from bs4 import BeautifulSoup
import os
from chapter1 import chapter2
from glob import glob


"""Worm guard instructions came as .vob files in dvd format. 
The were converted to .mkv files with the powershell script 
included in the repo called "convertvobfiles.ps1"""

class ScrapeLapelGuard:
    
    def __init__(self,chapter,html):
        
        self.chapter = chapter
        self.html = html
        
    def get_titles(self):
        
        soup = BeautifulSoup(self.html,'html.parser')
        titles = [text for text in soup.stripped_strings if "Chapter" not in text]
        titles = [i for i in titles if len(i)>6]
        titles = [i.replace("50/50","FiftyFifty") for i in titles]
        titles = [i.replace(":"," - ") for i in titles]
    
    
        return titles

    def make_chapter_folder(self):
        new_folder_path = "C:\\Users\\Vince\\Desktop\\WormGuard\\"+self.chapter
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
        return new_folder_path
    
    def get_duration(self):
        soup = BeautifulSoup(self.html,'html.parser')
        titles = [text for text in soup.stripped_strings if "Chapter" not in text]
        duration = [i for i in titles if len(i) < 6]
        return duration

def getfiles(filepath):
    return list(glob(filepath))
    
if __name__=='__main__':
    
    disk2 = ScrapeLapelGuard("chapter2", chapter2)
    titles = disk2.get_titles()
    duration = disk2.get_duration()
    folder = disk2.make_chapter_folder()
    
    old = getfiles("C:\\Users\\Vince\\Desktop\\WormGuard\\*.mkv")
    
    for oldfile,newfile,time in zip(old,titles,duration):
        time = time.replace(':', '-')
        
        os.rename(oldfile,folder+'\\'+str(newfile)+"_"+str(time)+".mkv")