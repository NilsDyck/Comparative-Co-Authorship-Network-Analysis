import os, re, csv, urllib.request, urllib.error, urllib.parse, pandas as pd
from bs4 import BeautifulSoup

#abstract funtion for later use
def get_abstract(site):
    soup = BeautifulSoup(site, 'html.parser')
    abstract = soup.find(class_ = 'c-article-section__content')
    abstract = abstract.find('p')
    abstract = str(abstract).replace(";",".") #for the csv-file there must not be any semicola in the abstracts
    abstract = re.sub("<.*?>","",abstract) #no html-tag should survive this action.
    abstract = abstract.replace("\n","")
    return abstract

#import all the data we need
files = os.scandir('data/raw/DCFS')
sites = []
for entry in files:
    with open(os.path.join('data/raw/DCFS', entry.name), 'r') as f:
       html = f.read()
       sites.append(html)

#initiate file to save data
with open('data/processed/DCFS-DCFS.csv', 'w') as f:
    f.write('Name;Title;Co-Authors;Pagintation;Published in;LNCS-link;Abstract\n')

for site in sites:
    #cook the soup for every conference site
    soup = BeautifulSoup(site, 'html.parser')
    print('got soup')
    #find all the papers
    papers = soup.find_all(class_='entry inproceedings')
    for paper in papers:
        #collect simple data
        authors = paper.find_all(itemprop='author')
        title = str(paper.find(class_="title").string)
        title = title.replace(';',':')#all semicola have to be replaced with double-dots
        pagination = paper.find_all(itemprop="pagination")
        datePublished = paper.find_all(itemprop="datePublished")
        print('got simple data')
        #get link to springer site
        # abstract_link = paper.find(class_='ee')
        # abstract_link = abstract_link.find(itemprop='url')
        # abstract_link = str(abstract_link)
        # abstract_link = re.search('<.*?>', abstract_link).group()
        # abstract_link = re.search('https://.*?"', str(abstract_link)).group()
        # abstract_link = abstract_link.replace('"', '')
        # response = urllib.request.urlopen(abstract_link)
        # abstract_site = response.read().decode('UTF-8')
        # abstract = get_abstract(abstract_site)
        # print('got abstract')
        #make a list of co-authors
        strings = []
        for author in authors:
            names = author.find_all(itemprop='name')
            for name in names:
                strings.append(name.string)
        #write data into csv-file        
        f = open('data/processed/DCFS-DCFS.csv', 'a')
        for i in range(len(strings)):
            f.write(strings[i]+';'+title+';')
            co_authors = ''
            for j in range(len(strings)):
                if j != i:    
                    co_authors += strings[j]+', '
            co_authors = co_authors[:-2]#remove ', ' at the end
            f.write(co_authors+';')
            f.write(str(pagination)+';'+str(datePublished)+'\n')#';'+abstract_link+';'+abstract+'\n')
        f.close()
