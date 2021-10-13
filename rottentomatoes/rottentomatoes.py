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
