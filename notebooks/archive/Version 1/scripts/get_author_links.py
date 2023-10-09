#get the site of each author who published at CIAA/DLT/DCFS. Make sure to check if the right datapath is given.

import os, re, urllib.request, urllib.error, urllib.parse

from bs4 import BeautifulSoup

#make list of conferneces 
files = os.scandir('data/raw/CIAA')
conferences = []
for entry in files:
    #print(entry.name)
    with open(os.path.join('data/raw/CIAA', entry.name), 'r') as f:
        conferences.append(f.read())
#iterate over list of conferences to find every author from each conference
authors = []
for conference in conferences:
    soup = BeautifulSoup(conference, 'html.parser')
    list = soup.find_all(itemprop = 'author')
    for entry in list:    
        authors.append(entry)

#create a list of authors
author_list = []
for author in authors:
    author_list.append(author.find(href = re.compile('https://dblp.uni-trier.de/pid*')))

author_set = set(author_list) #to remove duplicates

f = open('data/raw/everything/ciaa_author_links.csv', 'a') #make sure there is no similar file or an empty file
f.write('URL\n')
for entry in author_set:
    found = re.search('href=".*?"', str(entry)).group()
    found = found.replace('href="', '')
    found = found.replace('"', '')
    f.write(repr(found)+'\n')
f.close

# #download the html-code of each author-site
# for entry in author_set:
#     #As stated in Turkel, William J. / Crymble, Adam (2012): Downloading Web Pages with Python. Programming Historian. Online available at: https://programminghistorian.org/en/lessons/working-with-web-pages; last edit: 17.11.2021; last access: 06.10.2022:
#     response = urllib.request.urlopen(entry)
#     webContent = response.read().decode('UTF-8')
#     soup = BeautifulSoup(webContent, 'html.parser')
#     name = soup.find(class_='name primary')
#     name = name.string
#     with open('data/raw/CIAA/'+name+'.html', 'w') as f:
#         f.write(repr(soup))