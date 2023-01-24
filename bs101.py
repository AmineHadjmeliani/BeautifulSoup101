from bs4 import BeautifulSoup 
import requests 

url = 'https://subslikescript.com/movie/Titanic-120338'

resp = requests.get(url)
# print(resp) ## >>> <Response [200]> 

content = resp.text

## we use as parser Lxml
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box =  soup.find('article', class_='main-article')

## Instead of using soup we use box
title = box.find('h1').get_text()

## we use the strip and split methods
transcript= box.find('div', class_='full-script').get_text(strip=True, separator=' ')

## create a txt file to store the data cd
with open(f'{title}.txt', 'w', encoding="utf-8") as f:
    f.write(transcript)

