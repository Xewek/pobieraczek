import pytube
import bcolors
import os
import sys
from colorama import init
init(strip=not sys.stdout.isatty())
from termcolor import cprint
from pyfiglet import figlet_format
from pytube.cli import on_progress
from alive_progress import alive_bar
import time

#logo

cprint(figlet_format('pobie', font='starwars'),
       'blue', attrs=['bold'])
cprint(figlet_format('raczek', font='starwars'),
       'blue', attrs=['bold'])

print(bcolors.OK+ "Wklej link do wideo na YT" + bcolors.ENDC)
url = input(bcolors.OK+"link: "+bcolors.ENDC+bcolors.BLUE)

#folder
if not os.path.exists("Pobieraczek"):
       os.mkdir("Pobieraczek")

youtube = pytube.YouTube(url, on_progress)
tytul = youtube.title
print(bcolors.OKMSG+"  Trwa pobieranie wideo o nazwie: "+bcolors.ENDC+bcolors.BLUE+tytul)

for on_progress in 1000, 1000, 0:
   with alive_bar(on_progress) as bar:
        for i in range(1000):
            time.sleep(.006)
            bar()  
    
#rodzielczosc 
video = youtube.streams.get_highest_resolution()
video.download('./Pobieraczek')
#print("Pobrano: "+on_progress)

   
   
   
   
'''    
for video.download in 1000, 1000, 0:
   with alive_bar(video.download) as bar:
        for i in range(1000):
            time.sleep(.006)
            bar()'''
#pasek ladowania
'''def pasek():
    for i in range(1000):
        ... #progres przedmioty jak zwykle
        yield #'''
