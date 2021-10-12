from bs4 import BeautifulSoup
import requests
import pandas as pd

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

# test_links = ["https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=H7D50XFFRX3TVJ6101GY&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1","https://www.imdb.com/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=RK62CTDRG3FZG0FGMMT6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2","https://www.imdb.com/title/tt0071562/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=RK62CTDRG3FZG0FGMMT6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_3","https://www.imdb.com/title/tt0468569/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=RK62CTDRG3FZG0FGMMT6&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_4"]

# --------- Scraping Data ---------


movieNumber = 1
for link in fullLinks:
    dataDict = {}    
    url = requests.get(link)
    soup = BeautifulSoup(url.content,"lxml")
    rating = soup.find("span",class_="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV").text.strip()
    dataDict['Movie Name'] = soup.find("h1").text.strip()
    dataDict['Rating'] = f"{rating}/10"
    dataDict['People Voted'] = soup.find("div",class_="AggregateRatingButton__TotalRatingAmount-sc-1ll29m0-3 jkCVKJ").text.strip()
    try:
        dataDict['Popularity'] = soup.find("div",class_="TrendingButton__TrendingScore-bb3vt8-1 gfstID").text.strip()
    except:
        dataDict['Popularity'] = "Not Specified"
    try:
        dataDict['Category'] = soup.find("span",class_="ipc-chip__text").text.strip()
    except:
        dataDict['Category'] = "Not Specified"
    try:
        dataDict['Director'] = soup.find("a",class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text.strip()
    except:
        dataDict['Director'] = "Not Specified"
    try:
        dataDict['Critic Reviews'] = soup.find("span",class_="score").text.strip()
    except:
        dataDict['Critic Reviews'] = "Not Specified"
    try:
        dataDict['Metascore'] = soup.find("span",class_="score-meta").text.strip()
    except:
        dataDict['Metascore'] = "Not Specified"
    try:
        dataDict['Rewards'] = soup.find("li",attrs={"data-testid":"award_information"}).text.strip()
    except:        
        dataDict['Rewards'] = "Not Specified"
    try:
        budget = soup.find("li",attrs={"data-testid":"title-boxoffice-budget"}).text.strip().split('$')[-1]
        dataDict['Budget'] = f"${budget}"
    except:
        dataDict['Budget'] = "Not specified"
    try:
        gross_worldwide = soup.find("li",attrs={"data-testid":"title-boxoffice-cumulativeworldwidegross"}).text.strip().split('$')[-1]
        dataDict['Gross Worldwide'] = f"${gross_worldwide}"
    except:
        dataDict['Gross Worldwide'] = "Not specified"
    try:
        dataDict['Description'] = soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text.strip()
    except:
        dataDict['Description'] = "Not Specified"

    masterList.append(dataDict)

    print(f"finished movie #{movieNumber} {dataDict['Movie Name']}")
    movieNumber += 1

# --------- Scraping Data End ---------

# --------- Outputing to Excel ---------

df = pd.DataFrame(masterList)
File_Name = "imdb_data"
df.to_csv(f"{File_Name}.csv",index=False,columns=["Movie Name","Rating","Rating","Category","Description","Director"])
datatoexcel = pd.ExcelWriter(f"{File_Name}.xlsx",engine='xlsxwriter')
df.to_excel(datatoexcel,index=False)
datatoexcel.save()
print("\nData Output completed.")
print(f"File names: {File_Name}.xlsx, {File_Name}.csv")

# --------- Outputing to Excel End ---------