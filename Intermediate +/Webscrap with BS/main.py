from bs4 import BeautifulSoup
#import lxml
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text,"lxml")

containers = soup.find_all(class_="article-title-description__text")
list = []

for container in containers:
    movie_name = container.h3.text
    list.append(movie_name)

list.reverse()
with open("movies.txt", "w") as f:
    for item in list:
        f.write(item + '\n')