#   get the pubications from one author of your choice
#   Nils Dyck, 28.04.2023
import re, os, pandas as pd
from bs4 import BeautifulSoup

# # _________________ CIAA code __________________________________

# # with open('data/raw/CIAA/authors/Andreas Malcher.html','r') as f:
# #     site = f.read()

# # soup = BeautifulSoup(site, 'html.parser')
# # name = 'Markus Holzer'
# # papers = soup.find_all(class_=re.compile('entry.*toc'))
# # print(len(papers))

# # titles = []
# # with open('test.txt','w') as f:
# #     for paper in papers:
# #         title = str(paper.find(class_='title'))
# #         titles.append(title)
# #         f.write(str(paper)+'\n')

# author_sites = os.listdir('data/raw/CIAA/authors')

# df = pd.read_csv('data/processed/CIAA-authors.csv',sep=';')
# names = df['Name'].to_list()
# urls = df['URL'].to_list()

# # author_links = pd.read_csv('data/processed/CIAA-authors_sorted.csv', sep=';')
# # author_names = author_links['Name'].to_list()
# # author_links = author_links['URL'].to_list()

# #initiate csv-file for later saving
# with open('data/processed/DATASET2.csv', 'w') as f:
#     f.write('Key;Author-Key;Author;Author-URL;Title;Co-Authors;Co-Author-URLs;Pagination;Year;Venue\n')

# #funcitons for cleaning up strings
# def clean_name(name):
#     res = name.replace('dblp: ','')
#     res = res.replace('<title>','')
#     res = res.replace('</title>','')
#     name = re.sub('[0-9]*?', '', res)
#     last = res[len(res)-1]
#     if last == ' ':
#         res = res[:-1]
#     return res

# counter = 0
# paper_key = 0
# for site in author_sites:
#     key = int(site.replace('.html',''))
#     print(key)
#     with open(os.path.join('data/raw/CIAA/authors',site),'r') as f:
#         html_code = f.read()
#     soup = BeautifulSoup(html_code, 'html.parser')
#     #the name of the current author
#     name = names[key]
#     print(name)
#     # name = soup.title
#     # name = clean_name(str(name))
#     url = urls[key]
#     print(url)
#     #find every paper of the current author
#     papers = soup.find_all(class_=re.compile('entry.*toc'))
#     #print(len(papers))
#     for paper in papers:
#         #print('paper')
#         authors = paper.find_all(itemprop='author')
#         #print(authors)
#         #title = str(paper.find(class_="title").string)
#         title = str(paper.find(class_="title"))
#         title = re.sub('<.*?>','',title)
#         title = title.replace(';',':')#all semicola have to be replaced with double-dots
#         pagination = paper.find(itemprop="pagination")
#         datePublished = paper.find(itemprop="datePublished")
#         venue = paper.find(itemprop='isPartOf')
#         #venue = venue.find(itemprop='name').string
#         co_authors = [author.find_all(itemprop='name') for author in authors]
#         co_author_urls = [author.find_all(itemprop='url') for author in authors]
#         with open('data/processed/DATASET2.csv', 'a') as f:
#             f.write(str(paper_key)+';'+str(key)+';'+name+';'+url+';'+title+';'+str(co_authors)+';'+repr(co_author_urls)+';'+repr(pagination)+';'+repr(datePublished)+';'+repr(venue)+'\n')
#         paper_key += 1
#     counter += 1
#     print(str(counter))

# # with open('data/processed/dataset.csv','w') as f:
# #     f.write('Name;Title;Co-Authors;Co-Author URLs;Pagination;Date Published;Venue\n')

# # erg = 0
# # i = 0
# # for file in files:
# #     #print(file)
# #     with open(file, 'r') as f:
# #         site = f.read()
# #     soup = BeautifulSoup(site, 'html.parser')
# #     name = str(file)
# #     papers = soup.find_all(class_=re.compile('entry.*toc'))
# #     print(i)
# #     i += 1
# #     titles = []
# #     with open('data/processed/dataset.csv','a') as f:
# #         for paper in papers:
# #             authors = paper.find_all(itemprop='author')
# #             title = str(paper.find(class_="title").string)
# #             title = title.replace(';',':')#all semicola have to be replaced with double-dots
# #             pagination = paper.find(itemprop="pagination")
# #             pagination = str(pagination).replace(';',':')
# #             datePublished = paper.find(itemprop="datePublished")
# #             datePublished = str(datePublished).replace(';',':')
# #             venue = paper.find(itemprop='isPartOf')
# #             venue = str(venue).replace(';',':')
# #             #venue = venue.find(itemprop='name').string
# #             co_authors = [author.find_all(itemprop='name') for author in authors]
# #             co_author_urls = [author.find_all(itemprop='url') for author in authors]
# #             # title = str(paper.find(class_='title'))
# #             # titles.append(title)
# #             # f.write(str(paper)+'\n')
# #             f.write(str(name)+';'+str(title)+';'+str(co_authors)+';'+str(co_author_urls)+';'+str(pagination)+';'+str(datePublished)+';'+str(venue)+'\n')
# os.system('say "Fertig. Fertig. Fertig. Komm mal gucken, Nils."')   

# _________________ DCFS code __________________________________

author_sites = os.listdir('data/raw/DCFS/authors')

df = pd.read_csv('data/processed/DCFS-authors.csv',sep=';')
names = df['Name'].to_list()
urls = df['URL'].to_list()

# author_links = pd.read_csv('data/processed/CIAA-authors_sorted.csv', sep=';')
# author_names = author_links['Name'].to_list()
# author_links = author_links['URL'].to_list()

#initiate csv-file for later saving
with open('data/processed/DCFS-ALL.csv', 'w') as f:
    f.write('Key;Author-Key;Author;Author-URL;Title;Co-Authors;Co-Author-URLs;Pagination;Year;Venue\n')

#funcitons for cleaning up strings
def clean_name(name):
    res = name.replace('dblp: ','')
    res = res.replace('<title>','')
    res = res.replace('</title>','')
    name = re.sub('[0-9]*?', '', res)
    last = res[len(res)-1]
    if last == ' ':
        res = res[:-1]
    return res

counter = 0
paper_key = 0
for site in author_sites:
    key = int(site.replace('.html',''))
    print(key)
    with open(os.path.join('data/raw/DCFS/authors',site),'r') as f:
        html_code = f.read()
    soup = BeautifulSoup(html_code, 'html.parser')
    #the name of the current author
    name = names[key]
    print(name)
    # name = soup.title
    # name = clean_name(str(name))
    url = urls[key]
    print(url)
    #find every paper of the current author
    papers = soup.find_all(class_=re.compile('entry.*toc'))
    #print(len(papers))
    for paper in papers:
        #print('paper')
        authors = paper.find_all(itemprop='author')
        #print(authors)
        #title = str(paper.find(class_="title").string)
        title = str(paper.find(class_="title"))
        title = re.sub('<.*?>','',title)
        title = title.replace(';',':')#all semicola have to be replaced with double-dots
        pagination = paper.find(itemprop="pagination")
        datePublished = paper.find(itemprop="datePublished")
        venue = paper.find(itemprop='isPartOf')
        #venue = venue.find(itemprop='name').string
        co_authors = [author.find_all(itemprop='name') for author in authors]
        co_author_urls = [author.find_all(itemprop='url') for author in authors]
        with open('data/processed/DCFS-ALL.csv', 'a') as f:
            f.write(str(paper_key)+';'+str(key)+';'+name+';'+url+';'+title+';'+str(co_authors)+';'+repr(co_author_urls)+';'+repr(pagination)+';'+repr(datePublished)+';'+repr(venue)+'\n')
        paper_key += 1
    counter += 1
    print(str(counter))

# with open('data/processed/dataset.csv','w') as f:
#     f.write('Name;Title;Co-Authors;Co-Author URLs;Pagination;Date Published;Venue\n')

# erg = 0
# i = 0
# for file in files:
#     #print(file)
#     with open(file, 'r') as f:
#         site = f.read()
#     soup = BeautifulSoup(site, 'html.parser')
#     name = str(file)
#     papers = soup.find_all(class_=re.compile('entry.*toc'))
#     print(i)
#     i += 1
#     titles = []
#     with open('data/processed/dataset.csv','a') as f:
#         for paper in papers:
#             authors = paper.find_all(itemprop='author')
#             title = str(paper.find(class_="title").string)
#             title = title.replace(';',':')#all semicola have to be replaced with double-dots
#             pagination = paper.find(itemprop="pagination")
#             pagination = str(pagination).replace(';',':')
#             datePublished = paper.find(itemprop="datePublished")
#             datePublished = str(datePublished).replace(';',':')
#             venue = paper.find(itemprop='isPartOf')
#             venue = str(venue).replace(';',':')
#             #venue = venue.find(itemprop='name').string
#             co_authors = [author.find_all(itemprop='name') for author in authors]
#             co_author_urls = [author.find_all(itemprop='url') for author in authors]
#             # title = str(paper.find(class_='title'))
#             # titles.append(title)
#             # f.write(str(paper)+'\n')
#             f.write(str(name)+';'+str(title)+';'+str(co_authors)+';'+str(co_author_urls)+';'+str(pagination)+';'+str(datePublished)+';'+str(venue)+'\n')
os.system('say "Fertig. Fertig. Fertig. Komm mal gucken, Nils."')   