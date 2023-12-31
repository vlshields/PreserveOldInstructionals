# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 21:18:17 2023

@author: Vince
"""

from os import listdir
from os.path import isfile, join

def get_files_list():
    mypath = r"C:\Users\Vince\Desktop\WormGuard"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

if __name__ == "__main__":
    
    print(get_files_list())