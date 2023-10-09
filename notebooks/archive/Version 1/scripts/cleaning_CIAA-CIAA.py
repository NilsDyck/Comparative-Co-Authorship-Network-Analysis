import os, re, pandas as pd
from bs4 import BeautifulSoup

#read data
datapath = 'data/processed/CIAA-CIAA.csv'
sep_parameter = ';'

data = pd.read_csv(datapath, sep=sep_parameter)

#make lists of every category
authors = data['Name'].to_list()
titles = data['Title'].to_list()
co_authors = data['Co-Authors'].to_list()
paginations = data['Pagintation'].to_list()
published_ins = data['Published'].to_list()
venues = data['Venue'].to_list()
# abstract_sites = data['LNCS-link'].to_list()
# abstracts = data['Abstract'].to_list()

#clean co-authors
# for i in range(len(co_authors)):
#     co_authors[i] = str(co_authors[i]).split(', ')
# for i in range(len(co_authors)):
#     for j in range(len(co_authors[i])):
#         co_authors[i][j] = co_authors[i][j].replace('nan', '')

#clean paginations
paginations_clean = []
for pagination in paginations:
    p = repr(pagination)
    p_clean = re.search('>.*?<', p).group()
    p_clean = p_clean.replace('<', '')
    p_clean = p_clean.replace('>', '')
    paginations_clean.append(p_clean)

#clean published-ins
published_ins_clean = []
for published_in in published_ins:
    p_clean = re.search('"[0-9]*?"', published_in).group()
    p_clean = p_clean.replace('"', '')
    published_ins_clean.append(p_clean)

#cleaning venues
venues_clean = []
for venue in venues:
    v_clean = venue.replace('dblp: ','')
    v_clean = v_clean.replace('<title>','')
    v_clean = v_clean.replace('</title>','')
    venues_clean.append(v_clean)    

#initiate file to save cleaned data
with open('data/cleaned/CIAA-CIAA.csv', 'w') as f:    
    f.write('Author;Title;Co-Authors;Pagination;Published;Venue\n')#LNCS-link;Abstract\n')

#write the data into the file
for i in range(len(authors)):
    with open('data/cleaned/CIAA-CIAA.csv', 'a') as f:
        f.write(str(authors[i])+';'+str(titles[i])+';'+str(co_authors[i])+';'+str(paginations_clean[i])+';'+str(published_ins_clean[i])+';'+venues_clean[i]+'\n')#+str(abstract_sites[i])+';'+str(abstracts[i])+'\n')