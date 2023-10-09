#Downlaod the html-code for every conference of DLT
import os, re, csv, urllib.request, urllib.error, urllib.parse, pandas as pd
from bs4 import BeautifulSoup

conference_url = 'https://dblp.uni-trier.de/db/conf/dlt/index.html'

#cook the soup
response = urllib.request.urlopen(conference_url)
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent, 'html.parser')

# #save conference site
# with open('data/raw/DCFS/DCSF_conference-site.html', 'w') as f:
#     f.write(repr(soup))

#As the urls from the conferences are pretty similliar, we compute them with a loop
urls = [
    'https://dblp.uni-trier.de/db/conf/dlt/dlt'+str(i)+'.html' for i in range(2001,2023)
]

#cook the soup for every url and save the html-code into the correct file
year = 2001
for url in urls:
    response = urllib.request.urlopen(url)
    webContent = response.read().decode('UTF-8')
    soup = BeautifulSoup(webContent, 'html.parser')   
    with open('data/raw/DLT/dlt'+str(year)+'.html', 'w') as f:
        f.write(repr(soup))
    print(year)
    year += 1

#The DLTs from 2000 and earlier do not match the pattern, so we have to treat them by their own
response = urllib.request.urlopen('https://dblp.uni-trier.de/db/conf/dlt/wlc2000.html')
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent, 'html.parser')   
with open('data/raw/DLT/wlc2000.html', 'w') as f:
    f.write(repr(soup))
response = urllib.request.urlopen('https://dblp.uni-trier.de/db/conf/dlt/dlt1999.html')
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent, 'html.parser')   
with open('data/raw/DLT/dlt1999.html', 'w') as f:
    f.write(repr(soup))
response = urllib.request.urlopen('https://dblp.uni-trier.de/db/conf/dlt/dlt1997.html')
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent, 'html.parser')   
with open('data/raw/DLT/dlt1997.html', 'w') as f:
    f.write(repr(soup))
response = urllib.request.urlopen('https://dblp.uni-trier.de/db/conf/dlt/dlt1995.html')
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent, 'html.parser')   
with open('data/raw/DLT/dlt1995.html', 'w') as f:
    f.write(repr(soup))
response = urllib.request.urlopen('https://dblp.uni-trier.de/db/conf/dlt/dlt1993.html')
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent, 'html.parser')   
with open('data/raw/DLT/dlt1993.html', 'w') as f:
    f.write(repr(soup))