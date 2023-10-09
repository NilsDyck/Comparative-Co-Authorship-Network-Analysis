#We are cleaning the DATASET
import pandas as pd, re
from bs4 import BeautifulSoup

#import data
data = pd.read_csv('data/processed/DATASET.csv', sep=';')

#make a list of each coloum
authors = data['Author'].to_list()
#author_urls = data['Author-URL'].to_list()
titles = data['Title'].to_list()
co_authors = data['Co-Authors'].to_list()
co_author_urls = data['Co-Author-URLs'].to_list()
paginations = data['Pagination'].to_list()
years = data['Year'].to_list()
venue = data['Venue'].to_list()

authors_clean = []
for entry in authors:
    entry = entry.replace(' 0001','')
    authors_clean.append(entry)

#clean co-authors
co_authors_clean = []
for entries in co_authors:
    entries = entries.split(',')
    new_entry = []
    for entry in entries:
        new = re.search('>.*?<', str(entry)).group()
        new = new.replace('<','')
        new = new.replace('>','')
        new_entry.append(new)
    new_entry = str(new_entry)
    new_entry = new_entry.replace('[','')
    new_entry = new_entry.replace(']','')
    new_entry = new_entry.replace('\'','')    
    co_authors_clean.append(new_entry)
print(co_authors_clean[1])

#clean co_author_urls
co_author_urls_clean = []
for i in range(len(co_author_urls)):
    co_author_urls[i] = co_author_urls[i].split(',')
    # print(len(co_author_urls[i]))
    # print(co_author_urls[i])
    for j in range(1,len(co_author_urls[i])):
        # print(co_author_urls[i][j][1])
        # if co_author_urls[i][j][1] != '[' or co_author_urls[i][j][1] != ']':
        #     print(co_author_urls[i][j])
        #print('before: '+co_author_urls[i][j])
        if re.search('a', co_author_urls[i][j]):
            entry = re.search('https:.*?"', str(co_author_urls[i][j])).group()
            entry = entry.replace('"','')
            #print('after: '+entry)
            co_author_urls_clean.append(entry)
#print(co_author_urls_clean)

#clean paginations
paginations_clean = [BeautifulSoup(pagination, 'html.parser').string for pagination in paginations]
#print(paginations_clean)

#clean years
year_clean = [BeautifulSoup(year, 'html.parser').string for year in years]
#print(year_clean)

#Make a file with cleaned data
with open('data/cleaned/DATASET.csv', 'w') as f:
    f.write('Author;Title;Co-Authors;Co-Author-URLs;Pagination;Year;Venue\n')
    for i in range(len(authors)):
        f.write(authors_clean[i]+';'+titles[i]+';'+str(co_authors_clean[i])+';'+co_author_urls_clean[i]+';'+paginations_clean[i]+';'+year_clean[i]+';'+venue[i]+'\n')