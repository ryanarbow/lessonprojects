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
#soup.find_all("tr", class_="tcont")
rows = soup.find_all('tr', {'class': 'tcont'})

r = rows[0]

r.find_all('td')

columns = r.find_all('td')

#Need to pull columns 0,1,4,7,10 from each row

