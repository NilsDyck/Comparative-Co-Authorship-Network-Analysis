import urllib.request, urllib.error, urllib.parse, os

import re #for using regular expressions by finding the paper titles

from bs4 import BeautifulSoup

from config import dblp_url, lncs_url

name = input('Enter conference name: ')

#As stated in Turkel, William J. / Crymble, Adam (2012): Downloading Web Pages with Python. Programming Historian. Online available at: https://programminghistorian.org/en/lessons/working-with-web-pages; last edit: 17.11.2021; last access: 06.10.2022:
response = urllib.request.urlopen(dblp_url)
webContent = response.read().decode('UTF-8')

soup = BeautifulSoup(webContent, 'html.parser')

with open(os.path.join('data/raw/'+name,'dblp-conference-site.html'), 'w') as f:
    f.write(repr(soup))

#get links from the conferences
conferences = []
conferences.append('https://dblp.uni-trier.de/db/conf/wia/ciaa2022.html')
conferences.append('https://dblp.uni-trier.de/db/conf/wia/ciaa2021.html')
for i in range(2019, 1999, -1):
    conferences.append('https://dblp.uni-trier.de/db/conf/wia/ciaa'+str(i)+'.html')
for j in range(1999, 1995, -1):
    conferences.append('https://dblp.uni-trier.de/db/conf/wia/wia'+str(j)+'.html')

#download html-code of conference-sites
files=[]
for conference in conferences:
    response = urllib.request.urlopen(conference)
    webContent = response.read().decode('UTF-8')
    soup = BeautifulSoup(webContent, 'html.parser') 
    date = date = str(conference)
    date = re.search('wia/.*?\.html', date).group()
    date = date.replace('wia/','')
    files.append(date)
    with open(os.path.join('data/raw/'+name, date), 'w') as f:
        f.write(repr(soup))

with open(os.path.join('data/raw/'+name, files[0]), 'r') as f:
        code = f.read()    
soup = BeautifulSoup(code, 'html.parser')
papers = soup.find_all(class_ = 'ee')
del papers[0]
paper_links = []
for paper in papers:
    found = str(paper)
    found = re.search('"https://doi.org/.*?"', found).group()
    found = found.replace('"','')
    paper_links.append(found)
paper_links

#download LNCS html-code of all papers from each conference
import os #for creating directories
counter = 0
for file in files:
    #open file and cook the soup
    with open(os.path.join('data/raw/'+name, file), 'r') as f:
        code = f.read()    
    soup = BeautifulSoup(code, 'html.parser')
    papers = soup.find_all(class_ = 'ee') #find the LNCS-links of every paper from the conference
    del papers[0] #first link is always for LNCS-conference-site
    #extract the LNCS-links from the soup
    paper_links = []
    for paper in papers:
        found = str(paper)
        #print(str(re.search('"https://doi.org/.*?"', found)))
        found = re.search('"https://doi.org/.*?"', found).group()
        found = found.replace('"','')
        paper_links.append(found)
    #save html-Code from each paper site into the right folder
    directory_name = file.replace('.html', '')
    current_path = os.path.join('data/raw/'+name, directory_name)
    os.mkdir(current_path) #make directory for better overview
    for paper_link in paper_links:
        response = urllib.request.urlopen(paper_link)
        webContent = response.read().decode('UTF-8')
        soup = BeautifulSoup(webContent, 'html.parser')
        titles = soup.find_all(href = re.compile('/chapter/')) #collects titles
        #finding title
        title = soup.title
        title = str(title)
        title = title.replace('\xa0', ' ')
        title = re.sub("<.*?>", "", title) #no html-tag should survive this action.
        title = title.replace(' | SpringerLink', '')
        with open(os.path.join(current_path, title+'.html'), 'w') as f:
            f.write(repr(soup))
        counter += 1