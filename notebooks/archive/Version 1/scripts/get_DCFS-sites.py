#Downlaod the html-code for every conference of DCFS
import os, re, csv, urllib.request, urllib.error, urllib.parse, pandas as pd
from bs4 import BeautifulSoup

conference_url = 'https://dblp.uni-trier.de/db/conf/dcfs/index.html'

#cook the soup
response = urllib.request.urlopen(conference_url)
webContent = response.read().decode('UTF-8')
soup = BeautifulSoup(webContent, 'html.parser')
#save conference site
with open('data/raw/DCFS/DCSF_conference-site.html', 'w') as f:
    f.write(repr(soup))

#As the urls from the conferences are pretty similliar, we compute them with a loop
urls = [
    'https://dblp.uni-trier.de/db/conf/dcfs/dcfs'+str(i)+'.html' for i in range(2001,2023)
]

#cook the soup for every url and save the html-code into the correct file
year = 2001
for url in urls:
    #the following code is a little acrobatic but the urls from 2009 and 2010 are not matching the pattern and this was my straightforward solution
    if year != 2009 and year != 2010:
        response = urllib.request.urlopen(url)
    elif year == 2009:
        response = urllib.request.urlopen('https://dblp.uni-trier.de/db/series/eptcs/eptcs3.html')
    else:
        response = urllib.request.urlopen('https://dblp.uni-trier.de/db/series/eptcs/eptcs31.html')
    webContent = response.read().decode('UTF-8')
    soup = BeautifulSoup(webContent, 'html.parser')   
    with open('data/raw/DCFS/dcfs'+str(year)+'.html', 'w') as f:
        f.write(repr(soup))
    print(year)
    year += 1