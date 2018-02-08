# ####################################################################################################################################################
#  ______    _______   _______   _         _______   _______             _         _______   _______    ______    _____  
# (  __  \  (  ___  ) (  ____ ) | \    /\ (  ____ \ (  ___  ) |\     /| ( \       / ___   ) (  __   )  / ____ \  / ___ \ 
# | (  \  ) | (   ) | | (    )| |  \  / / | (    \/ | (   ) | | )   ( | | (       \/   )  | | (  )  | ( (    \/ ( (   ) )
# | |   ) | | (___) | | (____)| |  (_/ /  | (_____  | |   | | | |   | | | |           /   ) | | /   | | (____   ( (___) |
# | |   | | |  ___  | |     __) |   _ (   (_____  ) | |   | | | |   | | | |         _/   /  | (/ /) | |  ___ \   \____  |
# | |   ) | | (   ) | | (\ (    |  ( \ \        ) | | |   | | | |   | | | |        /   _/   |   / | | | (   ) )       ) |
# | (__/  ) | )   ( | | ) \ \__ |  /  \ \ /\____) | | (___) | | (___) | | (____/\ (   (__/\ |  (__) | ( (___) ) /\____) )
# (______/  |/     \| |/   \__/ |_/    \/ \_______) (_______) (_______) (_______/ \_______/ (_______)  \_____/  \______/ 
# ####################################################################################################################################################                                                                                                            
#  __     __             ____  U _____ u      ____      ____    ____       _      ____   U _____ u   ____     
#  \ \   /"/u  ___    U | __")u\| ___"|/     / __"| uU /"___|U |  _"\ uU  /"\  uU|  _"\ u\| ___"|/U |  _"\ u  
#   \ \ / //  |_"_|    \|  _ \/ |  _|"      <\___ \/ \| | u   \| |_) |/ \/ _ \/ \| |_) |/ |  _|"   \| |_) |/  
#   /\ V /_,-. | |      | |_) | | |___       u___) |  | |/__   |  _ <   / ___ \  |  __/   | |___    |  _ <    
#  U  \_/-(_/U/| |\u    |____/  |_____|      |____/>>  \____|  |_| \_\ /_/   \_\ |_|      |_____|   |_| \_\   
#    //   .-,_|___|_,-._|| \\_  <<   >>       )(  (__)_// \\   //   \\_ \\    >> ||>>_    <<   >>   //   \\_  
#   (__)   \_)-' '-(_/(__) (__)(__) (__)     (__)    (__)(__) (__)  (__|__)  (__|__)__)  (__) (__) (__)  (__) 
# ######################################################################################################################################################

# ################################### VIBE SCRAPER - (ANIDB.NET SCRAPER) BY VAISHNAV (darksoul2069@gmail.com) ##########################################

# ##############################################################

# This is my first python project I created all on my own so it's a little messy... Ok, it's messy af! I am Vaishnav, 16 Year Old Brat xD
# The Below Codes will definitely give you a Headache, so I recommend you not to read LMAO! (Unless U are planning to add more features to this stuff)
# If you are modifying this Project and distributing it online then Please Contact me at - "darksoul2069@gmail.com" and Tell me why u are modifying this project!
# This Project is Non-Profit, so don't accept it if somebody is selling this to you!

# ###################### VERY IMPORTANT ########################
# BEFORE MODIFYING/DISTRIBUTING THIS PROJECT PLEASE CONTACT ME - "darksoul2069@gmail.com"
# IF I GAVE YOU THE RIGHT TO MODIFY AND DISTRIBUTE, THEN PLEASE MENTION THE ORIGINAL SOURCE (THAT WOULD BE ME) OR MENTION THAT I VAISHNAV (darksoul2069@gmail.com) OWNS THIS PROJECT!
# ALSO SPECIFY THE CHANGES MADE TO THIS PROJECT BEFORE DISTRIBUTION/MODIFICATION
# ##############################################################

import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

print('==============================================' + '\n' + 'This Anime Scraper [for AniDB.net (http://anidb.net)] (Project/Scraper) was made by "Vaishnav J" if you face any problem you can mail me- "darksoul2069@gmail.com"' + '\n' + 'Hope you loved this python program/scraper!' + '\n' + 'Check out my anime site http://AnimeVibe.ml' + '\n' + '==============================================' + '\n')
url = input("Enter AniDB.net URL of the Anime you want to scrape/crawl (Example : https://anidb.net/perl-bin/animedb.pl?show=anime&aid=69) : " )
source_code = requests.get(url, headers=headers)
plain_text = source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
anime_name = soup.find("h1", {"class": "anime"})
anime_desc = soup.find("div", {"itemprop": "description"})
episodes = soup.find_all("td", {"class": "title name episode"})

image = soup.find_all('div',{"class": "g_section info"})
img = soup.find('img',{"itemprop": "image"})
lol = img.get('src')

anim = anime_name.text.strip()
print(anim)
anim = input("Give The File Name where you want to store the Anime Information (Anime Name): ")
anim_desc = anime_desc.text.strip()
max_num = int(input('Total or Number of Episodes to Fetch (Should be a number): '))
for i in range(max_num):
    episode = episodes[i].find("label", {"itemprop": "name"}) 
    print(f'Fetched- Episode {i+1}')
    with open(anim+".txt", "w") as f:
        f.write('==============================================================' + '\n' + '|||Vibe Scraper|||darksoul2069|||AniDB.net|||Vaishnav J|||'+'\n'+'Thank you for using Vibe Scraper for AniDB.net This Project was developed by Vaishnav (darksoul2069)'+'\n'+'|||http://AnimeVibe.ml|||' + '\n' + '==============================================================' + "\n" + 'Anime Name - ' + anim + "\n" + 'Poster/Image URL of ' + anim + ' - ' + lol + '\n')
        f.write('------------------' + "\n")
        f.write('Anime Description: ' + '\n' + '------------------' + "\n" + "\n" + anim_desc+"\n"+"\n")
        f.write('------------' + "\n" + 'Episode List' + "\n" + '------------' + "\n")
        for i in range(max_num):
            episode = episodes[i].find("label", {"itemprop": "name"})
            f.write('Episode ' + str(i+1) + ':' + ' ' + episode.text.strip() + "\n")

print('\n' + '============================' + '\n' + 'Success!!! Anime Information/Episodes is stored in ||"' + str(anim) + '.txt"||' + '\n' + 'Thank you for using Vibe Scraper for AniDB.net (by- Vaishnav (darksoul2069)' + '\n' + '============================')
