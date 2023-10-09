#Downlaod the html-code of each author whose link is found in the csv-file given by datapath. Files are saved in data/raw/[conference name].
#Make sure to specify from which conference you are getting the data.
import os, re, urllib.request, urllib.error, urllib.parse, pandas as pd

from bs4 import BeautifulSoup

#import author-sites from processed data
sep_parameter = ';'
datapath = 'data/raw/everything/ciaa_author_links.csv'
data = pd.read_csv(datapath, sep = sep_parameter)

#Download author-sites
urls = data['URL'].to_list()
sites = []
counter = 0
names = []
for url in urls:
    print(counter)
    counter += 1
    #As stated in Turkel, William J. / Crymble, Adam (2012): Downloading Web Pages with Python. Programming Historian. Online available at: https://programminghistorian.org/en/lessons/working-with-web-pages; last edit: 17.11.2021; last access: 06.10.2022:
    url = str(url).replace("'","",2)
    print(url)
    response = urllib.request.urlopen(url)
    webContent = response.read().decode('UTF-8')
    soup = BeautifulSoup(webContent, 'html.parser')
    name = soup.find(class_='name primary')
    name = name.string
    names.append(name)
    print(name)
    with open(os.path.join('data/raw/authors/CIAA', str(counter))+'.html', 'w') as f:
        f.write(repr(soup))
    with open('data/raw/authors/CIAA/index.csv', 'a') as f:
        f.write(repr(counter)+';'+repr(url)+'\n')