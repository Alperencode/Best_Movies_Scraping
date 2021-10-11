from bs4 import BeautifulSoup
import requests

url = "https://www.imdb.com/chart/top/"
url = requests.get(url)
soup = BeautifulSoup(url.content,"lxml")
masterList = []

# --------- Gathering Links ---------
shortLinks = []
fullLinks = []

td_Tags = soup.find_all("td",class_="titleColumn")

for td in td_Tags:
    link = td.a.get('href')
    shortLinks.append(link)

def Create_Links(link,number):
     return f"https://www.imdb.com{link}?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=H7D50XFFRX3TVJ6101GY&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_{number}"

number = 1
for link in shortLinks:
    fullLinks.append(Create_Links(link,number))
    number += 1

# Links in 'fullLinks' list now
# --------- Gathering Links End ---------

test_links = ["https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=H7D50XFFRX3TVJ6101GY&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1","https://www.imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=RK62CTDRG3FZG0FGMMT6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2","https://www.imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=RK62CTDRG3FZG0FGMMT6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3","https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=RK62CTDRG3FZG0FGMMT6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4"]

# --------- Scraping Data ---------
movieNumber = 1
for link in test_links:
    dataDict = {}
    url = requests.get(link)
    soup = BeautifulSoup(url.content,"lxml")
    dataDict['name'] = soup.find("h1").text.strip()
    rating = soup.find("span",class_="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV").text.strip()
    dataDict['full_Rating'] = f"{rating}/10"
    dataDict['popularity'] = soup.find("div",class_="TrendingButton__TrendingScore-bb3vt8-1 gfstID").text.strip()
    dataDict['category'] = soup.find("span",class_="ipc-chip__text").text.strip()
    dataDict['description'] = soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text.strip()
    dataDict['director'] = soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text.strip()
    

    masterList.append(dataDict)
    print(f"finished {movieNumber}")
    movieNumber += 1
    

# --------- Scraping Data End ---------