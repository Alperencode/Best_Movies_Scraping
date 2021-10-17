import requests
from bs4 import BeautifulSoup
import contextlib

# --------- Gatherin Links ---------
url = "https://www.rottentomatoes.com/top/bestofrt/"
url = requests.get(url)
soup = BeautifulSoup(url.content,"lxml")


movies = soup.find_all("tr")
movie_numbers = soup.find_all("td",class_="bold")
short_links = soup.find_all("a",class_="unstyled articleLink")
full_links = []

for link in short_links:
    if link.get("href")[1] == "m":
        url = f'https://www.rottentomatoes.com{link.get("href")}'
        full_links.append(url)

# --------- Gathering Links End ---------
for link in full_links[0:5]:
    url = requests.get(link)
    movie = BeautifulSoup(url.content,"lxml")
    name = movie.find("h1",attrs={"slot":"title"}).text.strip()
    # info = movie.find("p",attrs={"slot":"info"}).text.strip()
    whatToKnow = movie.find("span",attrs={"data-qa":"critics-consensus"}).text.strip().replace("\n","")
    infoSection = movie.find_all("li",class_="meta-row clearfix")
    rating = infoSection[0].find("div",class_="meta-value").text.strip().replace("\n","")
    category = infoSection[1].find("div",class_="meta-value").text.strip().replace("\n","").replace(" ","")
    originalLanguage = infoSection[2].find("div",class_="meta-value").text.strip().replace("\n","")
    director = infoSection[3].find("div",class_="meta-value").text.strip().replace("\n","")
    producer = infoSection[4].find("div",class_="meta-value").text.strip().replace("\n","")
    writers = infoSection[5].find("div",class_="meta-value").text.strip().replace("\n","")
    relaseDate_theaters = infoSection[6].find("div",class_="meta-value").text.strip()
    relaseDate_streaming = infoSection[7].find("div",class_="meta-value").text.strip()
    distributor = infoSection[8].find("div",class_="meta-value").text.strip()
    # soundMix = infoSection[9].find("div",class_="meta-value").text.strip()
    # aspectRatio = infoSection[10].find("div",class_="meta-value").text.strip()


    # tomatoMeter = movie.find("div",attrs={"tabindex":"'0'"}).text.strip()
    # print(tomatoMeter)
    print(f"Name: {name}")  
    # print(f"Info: {info}")
    # print(f"What to know: {whatToKnow}")
    print(f"Rating: {rating}")
    print(f"Category: {category}")
    print(f"Original Language: {originalLanguage}")
    print(f"Director: {director}")
    print(f"Producer: {producer}")
    print(f"Writers: {writers}")
    print(f"Relase date (Theaters): {relaseDate_theaters}")
    print(f"Realase date (Streaming): {relaseDate_streaming}")
    print(f"Distributor: {distributor}")
    # print(f"Soundmix: {soundMix}")
    # print(f"Aspect ratio: {aspectRatio}")