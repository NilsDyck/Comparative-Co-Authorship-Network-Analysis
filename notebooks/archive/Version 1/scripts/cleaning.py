import os, re, pandas as pd
from bs4 import BeautifulSoup

#read data as data
datapath = 'data/cleaned/collaboration_1.csv'
sep_parameter = ';'
data = pd.read_csv(datapath, sep=sep_parameter)

#separate data into lists for better cleaning
authors = data['Author'].to_list()
titles = data['Title'].to_list()
co_authors = data['Co-Authors'].to_list()
paginations = data['Pagination'].to_list()
published = data['Published in'].to_list()

#cleaning paginations
pages = []
for pagination in paginations:
    if pagination == 'None':
        pages.append('NULL')
    else:
        soup = BeautifulSoup(pagination, 'html.parser')
        pages.append(soup.string)

#cleaning dates of publishing
dates = []
for date in published:
    if date == 'None':
        dates.append('NULL')
    else:
        soup = BeautifulSoup(date, 'html.parser')
        dates.append(soup.string)

#saving cleaned data into csv-file
with open('data/cleaned/collaboration.csv', 'w') as f:
    f.write('Author;Title;Co-Authors;Pagination;Published in\n')
    for i in range(len(authors)):
        f.write(authors[i]+';')
        f.write(titles[i]+';')
        f.write(co_authors[i]+';')
        f.write(pages[i]+';')
        f.write(dates[i]+'\n')