# Preserve Old BJJ Instructionals

DVDs are easily lost and/or broken. If you have been practicing Jiu Jitsu for a while, you likely have instructional videos stored on physical dvds.
Older DVDs sometimes contain .vob files. VOB files often don't play on modern hardware and require conversion. This Repo is meant as a tool to quickly
convert vob files to mkv files and rename the titles of each instructional section. In this case, I use an old copy of "Keenan's Lapel Encyclopedia".

## Legal Disclaimer:


The code provided here is intended solely for the purpose of converting VOB files from legally acquired physical DVDs to MKV format and scraping associated titles from a website. The author of this code does not endorse, encourage, or support the unauthorized 
duplication or distribution of copyrighted material or any form of intellectual property theft.

Users are reminded to respect intellectual property rights and comply with applicable copyright laws in their jurisdiction. 
The code is to be used only with DVDs that the user has legally obtained, and any unauthorized use for the purpose of infringing on intellectual property rights is strictly prohibited.

The author shall not be held responsible for any misuse of this code or any legal consequences resulting from the unauthorized use of copyrighted material. 
Users are advised to use this code in compliance with applicable laws and regulations.

By using this code, you acknowledge and agree to abide by the terms of this legal disclaimer.
"""


## Getting Started
You will need physical dvds and a dvd reader. I use an external dvd player called "ASUS ZenDrive". This program was written in windows,
so keep in mind that some file naming conventions drivers may be different.

### Prerequisites

In addition to the libraries in requirments.txt, you will need an mkv converter: 
- Windows [MakeMKV](https://www.makemkv.com/))
- Linux[VLC](https://www.videolan.org/)

### Installing

Clone The Repo

``git clone https://github.com/vlshields/PreserveOldInstructionals``

Install requirements 
``pip install -r requirements.txt``
## Usage

``
  from scapetitles import ScrapeLapelGuard
  disk2 = ScrapeLapelGuard("chapter2", chapter2)
  titles = disk2.get_titles()
  duration = disk2.get_duration()
  folder = disk2.make_chapter_folder()
    
  old = getfiles("C:\\Your\\Path\\To\\Files\\*.mkv")
    
  for oldfile,newfile,time in zip(old,titles,duration):
      os.rename(oldfile,folder+'\\'+str(newfile)+"_"+str(time)+".mkv")``


