import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#Packages
from bs4 import BeautifulSoup
import requests

#Import page
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"


r = requests.get(url)
#Pass to Beautiful Soup
soup = BeautifulSoup(r.content)

#Return tags
table = soup.find_all('table')[6].find_all('tr', {'class': 'tcont'})

#Need to pull columns 0,1,4,7,10 from each row
for rows in table:
    col = rows.find_all('td')
    country = col[0].string
    year = col[1].string
    total = col[4].string
    men = col[7].string
    women = col[10].string
    

