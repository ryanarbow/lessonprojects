
# coding: utf-8

# In[14]:

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


# In[97]:

# First page to crawl
url = 'https://dogvacay.com/dog-boarding--tx--austin'


# In[5]:

# TODO: check if the page has multiple pages (most do, and use the url below to get the 2nd, 3rd, etc page data too)
# https://dogvacay.com/dog-boarding--tx--austin?p=2


# In[6]:

# TODO: set up a loop until you've checked all pages


# In[7]:

# TODO: set up a loop over other cities too


# In[16]:

# This gets the page from the web, and also waits one second after you do
# The one second wait is to make sure you don't accidentally make too many requests which is bad netiquette
r = requests.get(url)
time.sleep(1)


# In[17]:

# Make sure you got a 200 response, otherwise it indicates an error
r.status_code


# In[9]:

soup = BeautifulSoup(r.content)


# In[19]:

# Convert the text to a beautiful soup object
soup = BeautifulSoup(r.content)


# In[21]:

# Remeber the "inspect element" trick I showed you in Chrome?  Use that to find the data you want
sitters = soup.findAll('div', {'class': 'card-content'})
len(sitters)


# In[165]:

# Data extraction phase
# TODO: This is a work in progress.  You should have a go at getting it working.
# TODO: Pick which important fields you want to extract, find them, build the data frame

sitter = sitters[3]
times = []
fees = []
reviews = []
repeats = []
city = []
for sitter in sitters:
    response_time = sitter.findAll('div', {'class': 'icon-wrapper'})[0].text
    fee = sitter.findAll('div', {'class': 'price price--primary u-text-center'})
    reviews = sitter.find('span', {'class': 'vcard-review'})
    #repeats = sitter.findAll('div', {'class': 'icon-wrapper'})[0].text
    fees.append(fee)
    city.append('Austin')
    times.append(response_time)
    #reviews.append(reviews)

df = pd.DataFrame({'city': city, 'fee': fees, 'response_time': times, 'reviews' : reviews})
df


# In[166]:

for sitter in sitters:
    repeats = sitter.findAll('div', {'class': 'icon-wrapper'})


# In[167]:

repeats


# In[156]:

for sitter in sitters:
    repeats = sitter.findAll('div', {'class': 'icon-wrapper'})[1]


# In[175]:

for sitter in sitters:
    reviews = sitter.find('span', {'class': 'vcard-review'})


# In[177]:

reviews


# In[ ]:



