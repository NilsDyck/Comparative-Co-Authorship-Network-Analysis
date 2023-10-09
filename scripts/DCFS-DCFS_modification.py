# Some modifications to the DCFS-DCFS dataset are done, to make work easier.
# Nils Dyck, 31.05.2023

import pandas as pd

df = pd.read_csv('data/cleaned/DCFS-DCFS.csv', sep=';')
key_table = pd.read_csv('data/processed/DCFS-authors.csv', sep=';')

co_author_urls = df['Co-Author-URLs'].to_list()
author_keys = df['Author-Key'].to_list()
author_urls = df['Author-URL'].to_list()
title = df['Title'].to_list()
year = df['Year'].to_list()
pagination = df['Pagination'].to_list()

no_authors = []
for entries in co_author_urls:
    if entries == '[]': no_authors.append(1)
    else:
        entries = entries.replace('[','').replace(']','').replace('"','').replace("'",'') 
        entries = entries.split(', ')
        no_authors.append(len(entries)+1)

# co_author_keys = []
# i = 0
# for list in co_author_urls:
#     list = list.replace('[','').replace(']','').replace("'","").replace(' ','')
#     list = list.split(',')
#     list.append(author_keys[i])
#     co_author_keys.append(list)
#     i += 1

# paper_keys = []
# for entry in co_author_keys:
#     cak = []
#     for i in range(len(entry)-1):
#         if entry[i] != '': 
#             key_line = key_table.loc[key_table['URL']==entry[i]]
#             key = key_line['Key'].to_list()[0]
#             cak.append(int(key))
#     cak.append(entry[-1])
#     cak = sorted(cak)
#     paper_keys.append(cak)
# print(paper_keys[0])

# with open('data/cleaned/CIAA-CIAA_m.csv','w') as f: f.write('Authors;Title;Year;Pagination\n')

# for i in range(len(paper_keys)):
#     with open('data/cleaned/CIAA-CIAA_m.csv','a') as f: f.write(str(paper_keys[i])+';'+title[i]+';'+str(year[i])+';'+pagination[i]+'\n')

with open('data/cleaned/DCFS-DCFS_m2.csv','w') as f: f.write('Author;Title;Co-Authors;No Authors;Year;Pagination\n')

for i in range(len(co_author_urls)):
    with open('data/cleaned/DCFS-DCFS_m2.csv','a') as f: f.write(str(author_urls[i])+';'+title[i]+';'+str(co_author_urls[i])+';'+str(no_authors[i])+';'+str(year[i])+';'+pagination[i]+'\n')
