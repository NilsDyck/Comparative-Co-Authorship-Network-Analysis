#   rescale the script 'get_author_sites_2022.py' to get the author-sites from every CIAA conference
#   Nils Dyck, 28.04.2023

import re, webbrowser, os, urllib.request, urllib.error, urllib.parse, pandas as pd
from bs4 import BeautifulSoup

# files = os.scandir('data/raw/CIAA')
files = os.scandir('data/raw/DCFS')

# with open('data/processed/CIAA-authors.csv','w') as f:
#     f.write('Name;URL\n')

with open('data/processed/DCFS-authors.csv','w') as f:
    f.write('Name;URL\n')

for entry in files:
    with open(entry,'r') as f:
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

    #print(str(entry)+str(len(author_list)))

    # with open('data/processed/CIAA-authors.csv','a') as f:
    #     for i in range(len(author_links)):
    #         f.write(str(author_names[i])+';'+str(author_links[i])+'\n')
    with open('data/processed/DCFS-authors.csv','a') as f:
        for i in range(len(author_links)):
            f.write(str(author_names[i])+';'+str(author_links[i])+'\n')

#drop duplicates from the auhtor names and links
# df = pd.read_csv('data/processed/CIAA-authors.csv', sep=';')
df = pd.read_csv('data/processed/DCFS-authors.csv', sep=';')
df.drop_duplicates(inplace=True)
author_names = df['Name'].to_list()
author_links = df['URL'].to_list()
#df.to_csv('data/processed/CIAA-authors.csv', sep=';', index=False)

# os.mkdir('data/raw/CIAA/authors')
os.mkdir('data/raw/DCFS/authors')

print(len(author_links))

#df = pd.read_csv('data/processed/CIAA-authors.csv', sep=';')


# with open('data/processed/CIAA-authors.csv','w') as f:
#     f.write('Key;Name;URL\n')
with open('data/processed/DCFS-authors.csv','w') as f:
    f.write('Key;Name;URL\n')

for i in range(len(author_links)):
    print(author_names[i])
    response = urllib.request.urlopen(author_links[i])
    webContent = response.read().decode('UTF-8')
    # with open('data/raw/CIAA/authors/'+str(i)+'.html','w') as f:
    #     f.write(webContent)
    # with open('data/processed/CIAA-authors.csv','a') as f:
    #     f.write(str(i)+';'+str(author_names[i])+';'+author_links[i]+'\n')
    with open('data/raw/DCFS/authors/'+str(i)+'.html','w') as f:
        f.write(webContent)
    with open('data/processed/DCFS-authors.csv','a') as f:
        f.write(str(i)+';'+str(author_names[i])+';'+author_links[i]+'\n')