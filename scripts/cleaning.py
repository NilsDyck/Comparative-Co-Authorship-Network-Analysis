#   cleaning the processed dataset
#   Nils Dyck, 28.04.2023

import pandas as pd, re, os
from bs4 import BeautifulSoup

i = 100   

# df = pd.read_csv('data/processed/dataset.csv', sep=';')
df = pd.read_csv('data/processed/DCFS-ALL.csv', sep=';')

#cleaning names
names = df['Name'].to_list()
names_cleaned = []
for name in names:
    name = str(name).replace("<DirEntry '","").replace("'>","").replace(".html","")
    names_cleaned.append(name)

#cleaning co-authors
co_authors = df['Co-Authors'].to_list()
co_authors_cleaned = []
for co_author in co_authors:
    entries = []
    for entry in co_author:
        entry = str(entry)
        start_index = entry.find('>')
        # index = entry.find('<')
        end_index = entry.find('<',1)
        entry = entry[start_index+1:end_index]
        entries.append(entry)
    print(entries)
    co_authors_cleaned.append(entries)

#cleaning co-author URLs
urls = df['Co-Author URLs'].to_list()
urls_cleaned = []