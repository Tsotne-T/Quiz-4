from bs4 import BeautifulSoup
from time import sleep 
from random import randint
import requests
import csv

f = open('anime.csv', 'w', newline='\n')

anime_write = csv.writer(f)
anime_write.writerow(['Name'])

h = {'Accept-Language' : 'en-US'}
index = 0  

while index<250:           
    url = 'https://myanimelist.net/topanime.php?limit='+ str(index)

    r = requests.get(url, headers=h)
    content = r.text

    soup = BeautifulSoup(content , 'html.parser')
    # print(soup)

    all_anime_block = soup.find('h3', {'class':'hoverinfo_trigger'})

    #class_ = lister-list
    all_anime = all_anime_block.find('a')



    for name in all_anime:
        print(name)

    anime_write.writerow([name])

    index += 50

    sleep(randint(15,20))