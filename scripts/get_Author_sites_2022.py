# extract every author-site from authors who contributed to CIAA 2022
# Nils Dyck, 28.04.2023

import re, webbrowser, os, urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

with open('data/raw/CIAA/ciaa2022.html','r') as f:
    site = f.read()

soup = BeautifulSoup(site, 'html.parser')

#find every author's html-snipplet
author_list_raw = soup.find_all(itemprop = 'author')

#every author-site's link starts with ...pid
author_list = [entry.find(href = re.compile('https://dblp.uni-trier.de/pid*')) for entry in author_list_raw]

#extract the urls from the html extract
author_links = []
author_names = []
for entry in author_list:
    link = re.search('href=".*?"', str(entry)).group()
    link = link.replace('href="', '')
    link = link.replace('"', '')
    author_links.append(link)
    name = entry.find(itemprop='name')
    name = name.string
    author_names.append(name)

#remove duplicates
author_list = set(author_list)

print(len(author_list))
print(author_links)
print(author_names)
# for entry in author_links:
#      webbrowser.open(entry)

#os.mkdir('data/raw/CIAA/2022')
with open('data/processed/CIAA-authors_2022.csv','a') as f:
    f.write('Name;URL\n')
    for i in range(len(author_links)):
        # response = urllib.request.urlopen(author_links[i])
        # webContent = response.read().decode('UTF-8')
        f.write(str(author_names[i])+';'+str(author_links[i])+'\n')
