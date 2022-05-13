# Requests for handling HTTP get and other requests
import requests
import time # import for playing nice and not getting blocked
import pandas as pd
# from BeautifulSoup4 import BeatifulSoup #if installed through pip install BeautifulSoup4
# 
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
 
# lets combine the above cells into a function which will always get us columns
def getColList(soup):
    column_list = ["description","url"] # we decided to that we need these two column names no matter the html
    headline = soup.find("tr", {"id":"head_line"})
    headtds = headline.find_all("td")
    headcolumns = [el.text for el in headtds[1:]] # this will get all column names starting with 2nd in HTML
    column_list += headcolumns
    return column_list
 
# lets make a function from the above doodle and make it work on most pages on SS
def getRowList(soup):
    trows = soup.find_all('tr')
    aprows = [row for row in trows if row.get('id',"").startswith("tr_") and not row.get('id',"").startswith("tr_bnr") ]
    return aprows
 
def getRow(row,colist):
    row_tds = row.find_all('td')
    rowDict = {}
    if len(row_tds) < 3: # a little sanity check
        print("Hmm bad row")
        return rowDict
    
    rowDict[colist[0]] = row_tds[2].text # so the big assumption is that we always get description in 3rd column
    rowDict[colist[1]] = "https://ss.com" + row_tds[1].find('a').get('href')
    for td,key in zip(row_tds[3:],colist[2:]): 
        rowDict[key] = td.text
    return rowDict
 
# so if we know how to work on single row then we can do process multiple rows
def getRows(rowlist,colist):
    return [getRow(row, colist=colist) for row in rowlist] # so return a list of dictionaries
 
# so with this function I can get full dataframe from a single page on ss.com not only apartments
def getDFfromURL(url):
    # print("getting data from", url)
    req = requests.get(url)
    if req.status_code != 200:
        print("Request Fail with", req.status_code)
        return None # maybe return empty dataframe here
    soup = BeautifulSoup(req.text, 'lxml')
    column_names = getColList(soup)
    rowlist = getRowList(soup)
    rows = getRows(rowlist,colist=column_names)
    return pd.DataFrame(rows, columns=column_names)
 
def getAllLocalUrls(url):
    """Get a list of all urls including paginated pages"""
    results = [url] # default is just the url if no extra pages found, teiksim Bolderājai...
    req = requests.get(url)
    if req.status_code != 200:
        print(f"Bad response! {req.status_code}")
        return []
    soup = BeautifulSoup(req.text, 'lxml')
    # we just need a one element
    prevanchor = soup.find('a', {"rel":"prev"}) # find finds first match only
    if prevanchor == None: # means there is only one page of ads
        return results
    href = prevanchor.attrs.get('href')
    lastPageNum = int(href.split('/page')[-1].split('.html')[0])
    print("Last page is",lastPageNum)
    nurls = [f"{url}page{n}.html" for n in range(2,lastPageNum+1)]
    results += nurls
    return results
 
def get_all_ads_df(start_url, save_excel_path=None):
    df_list=[] # so we will save our dataframes in a list
    local_urls = getAllLocalUrls(start_url)
    for url in local_urls:
        print(f"Gathering data from {url}")
        df_list.append(getDFfromURL(url))
        time.sleep(0.3) # we need this to play nice! to avoid rate limit or IP ban!!
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html
    big_df = pd.concat(df_list) # then make a big dataframe from all the small dataframes
    if save_excel_path:
        big_df.to_excel(save_excel_path)
    return big_df
 
#### Task 1b
 
url = "https://www.ss.lv/lv/real-estate/flats/riga/dzeguzhkalns/sell/"
all_ads_df = get_all_ads_df(url)
 
floor_info = [int(floor.split("/")[0]) for floor in list(all_ads_df["Stāvs"])]
max_floor = max(floor_info)
print(f"No Dzegužkalna apkaimē pārdotajiem dzīvokļiem augstākais stāvs ir {max_floor}!")
 
#### Task 1c
all_ads_df.to_excel("Dzeguzkalns.xlsx")
 
#### Task 1d
all_price = [float(price.split()[0].replace(",","")) for price in all_ads_df["Cena"]]
plt.hist(all_price)
plt.xlabel("Cena, €")
plt.ylabel("Biežums")
plt.title("Dzīvokļu cenu histogramma Dzegužkalnā")
plt.show()
 
 
#### Task 2
 
url = "https://www.ss.lv/lv/transport/cars/opel/astra/sell/"
all_ads_df = get_all_ads_df(url)
all_price = [float(price.split()[0].replace(",","")) for price in all_ads_df["Cena"]]
plt.figure()
plt.hist(all_price)
plt.xlabel("Cena, €")
plt.ylabel("Biežums")
plt.title("Opel Astra cenu histogramma")
plt.show()