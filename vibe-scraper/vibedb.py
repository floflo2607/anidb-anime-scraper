# ####################################################################################################################################################
#  ______    _______   _______   _         _______   _______             _         _______   _______    ______    _____  
# (  __  \  (  ___  ) (  ____ ) | \    /\ (  ____ \ (  ___  ) |\     /| ( \       / ___   ) (  __   )  / ____ \  / ___ \ 
# | (  \  ) | (   ) | | (    )| |  \  / / | (    \/ | (   ) | | )   ( | | (       \/   )  | | (  )  | ( (    \/ ( (   ) )
# | |   ) | | (___) | | (____)| |  (_/ /  | (_____  | |   | | | |   | | | |           /   ) | | /   | | (____   ( (___) |
# | |   | | |  ___  | |     __) |   _ (   (_____  ) | |   | | | |   | | | |         _/   /  | (/ /) | |  ___ \   \____  |
# | |   ) | | (   ) | | (\ (    |  ( \ \        ) | | |   | | | |   | | | |        /   _/   |   / | | | (   ) )       ) |
# | (__/  ) | )   ( | | ) \ \__ |  /  \ \ /\____) | | (___) | | (___) | | (____/\ (   (__/\ |  (__) | ( (___) ) /\____) )
# (______/  |/     \| |/   \__/ |_/    \/ \_______) (_______) (_______) (_______/ \_______/ (_______)  \_____/  \______/ 
# ################################### VIBE SCRAPER - (ANIDB.NET SCRAPER) BY (darksoul2069@gmail.com) ##########################################

import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'} #User Agent cuz we are trynna scrape a site and the site will automatically block bots n stuff so u need this to bypass any kinda of blocked response

print('==============================================' + '\n' + 'This Anime Scraper [for AniDB.net (http://anidb.net)] (Project/Scraper) was made by darksoul2069 if you face any problem you can mail me- "darksoul2069@gmail.com"' + '\n' + 'Hope you loved this python program/scraper!' + '\n' + 'Check out my anime site https://animevibe.tv' + '\n' + '==============================================' + '\n')
url = input("Enter AniDB.net URL of the Anime you want to scrape/crawl (Example : https://anidb.net/perl-bin/animedb.pl?show=anime&aid=69) : " )
source_code = requests.get(url, headers=headers) #requesting the site's page source...
plain_text = source_code.text #turning the source code to a readable format :P
soup = BeautifulSoup(plain_text, "html.parser") #parsing the page source code...
anime_name = soup.find("h1", {"class": "anime"}) #fetching the anime title
anime_desc = soup.find("div", {"itemprop": "description"}) # fetching the summary/description.
episodes = soup.find_all("td", {"class": "title name episode"}) # getting the place where the episode titles are kept (here the episode titles are in a table)

image = soup.find_all('div',{"class": "g_section info"}) #getting div for getting the image source
img = soup.find('img',{"itemprop": "image"}) # getting the precise location of the animes cover.
lol = img.get('src') # getting the animes image url
# well everything is pretty easy to grasp and understandable until now xD
anim = anime_name.text.strip() # Getting the text as a string out of the html tag we grabbed as a whole 
print(anim)
anim = input("Give The File Name where you want to store the Anime Information (Anime Name): ") #Taking File name from the user as input
anim_desc = anime_desc.text.strip() # Stripping out the text from the html tags
max_num = int(input('Total or Number of Episodes to Fetch (Should be a number): ')) #letting user input the number of episodes to grab (titles only)
for i in range(max_num): #Setting a range to grab the lists of episode titles
    episode = episodes[i].find("label", {"itemprop": "name"}) #Grabbing the Episode Titles
    print(f'Fetched- Episode {i+1}')
    with open(anim+".txt", "w") as f: #Writing it to a text file
        f.write('==============================================================' + '\n' + '|||Vibe Scraper|||darksoul2069|||AniDB.net|||'+'\n'+'Thank you for using Vibe Scraper for AniDB.net'+'\n'+'||| http://AnimeVibe.xyz |||' + '\n' + '==============================================================' + "\n" + 'Anime Name - ' + anim + "\n" + 'Poster/Image URL of ' + anim + ' - ' + lol + '\n')
        f.write('------------------' + "\n")
        f.write('Anime Description: ' + '\n' + '------------------' + "\n" + "\n" + anim_desc+"\n"+"\n")
        f.write('------------' + "\n" + 'Episode List' + "\n" + '------------' + "\n")
        for i in range(max_num):
            episode = episodes[i].find("label", {"itemprop": "name"})
            f.write('Episode ' + str(i+1) + ':' + ' ' + episode.text.strip() + "\n")

print('\n' + '============================' + '\n' + 'Anime Information/Episodes is stored in ||"' + str(anim) + '.txt"||' + '\n' + '============================')
# AND YOU ARE DONE xD | ENJOY :/
