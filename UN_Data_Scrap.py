import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#Packages
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Import page
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

r = requests.get(url)

#Pass to Beautiful Soup
soup = BeautifulSoup(r.content)

#Return tags
table = soup.find_all('table')[6]
table1 = table.find_all('table')[1].find_all('tr', {'class': 'tcont'})

#Need to pull info from columns 0,1,4,7,10 from each row
records = []
for rows in table1:
    col = rows.find_all('td')
    country = col[0].string
    year = col[1].string
    total = col[4].string
    men = col[7].string
    women = col[10].string
    record = (country, year, total, men, women)
    records.append(record)
column_name = ['country', 'year', 'total', 'men', 'women']   
df = pd.DataFrame(records, columns = column_name)

