#Get all author information needed from dblp

import os, re, urllib.request, urllib.error, urllib.parse, pandas as pd

from bs4 import BeautifulSoup

#make list of author-sites
files = os.scandir('data/raw/CIAA/Authors')
author_sites = []
for entry in files:
    #print(entry.name)
    with open(os.path.join('data/raw/CIAA/Authors', entry.name), 'r') as f:
        author_sites.append(f.read())

names = []
counter = 0
for site in author_sites:
    print(counter)
    counter += 1
    soup = BeautifulSoup(site, 'html.parser')
    name = str(soup.title)
    name = name.replace('dblp: ', '')
    #name = re.sub(' [0-9]*?','',name)
    names.append(name)

datapath = 'data/processed/author_links.csv'
data = pd.read_csv(datapath, sep = ';')
links = data['URL'].to_list()

with open('data/processed/authors.csv', 'w') as f:
    f.write('Name;URL\n')
    for i in range(len(names)):
        f.write(names[i]+';'+links[i]+'\n')