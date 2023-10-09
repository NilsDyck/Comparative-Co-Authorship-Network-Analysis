# this script creates a dataset of any conference listed at DBLP (https://dblp.uni-trier.de) from the url of the conference site at DBLP. It contains every author who ever published at the conference with all publications.
import urllib.request, urllib.error, urllib.parse, os, re, pandas as pd
from bs4 import BeautifulSoup

class Dataset_Creation:

    def __init__(self, conference_url, path, venue):
            self.conference_url = conference_url
            self.path = path
            self.venue = venue
    
    def create_structure(self):
        os.mkdir(self.path+'raw')
        os.mkdir(self.path+'processed')
        os.mkdir(self.path+'cleaned')

    def get_conference_sites(self):
        response = urllib.request.urlopen(self.conference_url)
        webContent = response.read().decode('UTF-8')
        with open(self.path+'conference_site.html', 'w') as f:
            f.write(repr(webContent))
        conference_sites = re.findall('https://dblp.uni-trier.de/db/conf/.*?.html', webContent)
        for site in conference_sites:
            response = urllib.request.urlopen(site)
            webContent = response.read().decode('UTF-8')
            with open(self.path+'raw/'+site, 'w') as f:
                f.write(repr(webContent))
    
    def get_author_sites(self):

        files = os.scandir(self.path+'data/raw')

        with open(self.path+'data/processed/authors.csv','w') as f:
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

            with open(self.path+'data/processed/authors.csv','a') as f:
                for i in range(len(author_links)):
                    f.write(str(author_names[i])+';'+str(author_links[i])+'\n')

            #drop duplicates from the auhtor names and links
            df = pd.read_csv(self.path+'data/processed/authors.csv', sep=';')
            df.drop_duplicates(inplace=True)
            author_names = df['Name'].to_list()
            author_links = df['URL'].to_list()

            os.mkdir(self.path+'data/raw/authors')

            with open(self.path+'data/processed/authors.csv','w') as f:
                f.write('Key;Name;URL\n')

            for i in range(len(author_links)):
                response = urllib.request.urlopen(author_links[i])
                webContent = response.read().decode('UTF-8')
                with open(self.path+'data/raw//authors/'+str(i)+'.html','w') as f:
                    f.write(webContent)
                with open(self.path+'data/processed/DCFS-authors.csv','a') as f:
                    f.write(str(i)+';'+str(author_names[i])+';'+author_links[i]+'\n')

    def get_publications(self):

        author_sites = os.listdir(self.path+'data/raw/authors')

        df = pd.read_csv(self.path+'data/processed/authors.csv',sep=';')
        names = df['Name'].to_list()
        urls = df['URL'].to_list()

        #initiate csv-file for later saving
        with open(self.path+'data/processed/DATASET.csv', 'w') as f:
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
            with open(os.path.join(self.path+'data/raw/authors',site),'r') as f:
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
                with open(self.path+'data/processed/DATASET.csv', 'a') as f:
                    f.write(str(paper_key)+';'+str(key)+';'+name+';'+url+';'+title+';'+str(co_authors)+';'+repr(co_author_urls)+';'+repr(pagination)+';'+repr(datePublished)+';'+repr(venue)+'\n')
                paper_key += 1
            counter += 1
            print(str(counter))
        os.system('say "dataset created."')
        print("Dataset created.")   

    def cleaning(self):
        print()
        #import data
        data = pd.read_csv(self.path+'data/processed/DATASET.csv', sep=';')

        #make a list of each coloum
        keys = data['Key'].to_list()
        author_keys = data['Author-Key']
        authors = data['Author'].to_list()
        author_urls = data['Author-URL'].to_list()
        titles = data['Title'].to_list()
        co_authors = data['Co-Authors'].to_list()
        co_author_urls = data['Co-Author-URLs'].to_list()
        paginations = data['Pagination'].to_list()
        years = data['Year'].to_list()
        venues = data['Venue'].to_list()

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

        #clean co_author_urls
        co_author_urls_clean = []
        for entries in co_author_urls:
            entries = entries.split(',')
            new_entry = []
            for entry in entries:
                if re.search('href=".*"',entry):
                    found = re.search('href=".*html"',entry).group()
                    new = found.replace('href="','').replace('"','')
                    new_entry.append(new)
            co_author_urls_clean.append(new_entry)

        #clean paginations
        paginations_clean = [BeautifulSoup(pagination, 'html.parser').string for pagination in paginations]

        #clean years
        year_clean = [BeautifulSoup(year, 'html.parser').string for year in years]

        #clean venues
        venues_clean = [BeautifulSoup(venue, 'html.parser').string for venue in venues]

        no_authors = []
        for entries in co_author_urls_clean:
            if entries == '[]': no_authors.append(1)
            else:
                entries = entries.replace('[','').replace(']','').replace('"','').replace("'",'') 
                entries = entries.split(', ')
                no_authors.append(len(entries)+1)

        with open(self.path+'data/cleaned/BIG_DATASET.csv', 'w') as f:
            f.write('Key;Author-Key;Author;Author-URL;Title;Co-Authors;Co-Author-URLs;NoAuthors;Pagination;Year;Venue\n')
            for i in range(len(authors)):
                f.write(str(keys[i])+';'+str(author_keys[i])+';'+authors_clean[i]+';'+author_urls[i]+';'+titles[i]+';'+str(co_authors_clean[i])+';'+str(co_author_urls_clean[i])+';'+no_authors[i]+';'+paginations_clean[i]+';'+year_clean[i]+';'+venues_clean[i]+'\n')
        os.system('say"Finished cleaning."')
        print("Finished cleaning.")
    
    def small_dataset(self):
        df = pd.read_csv(self.path+'data/cleaned/DATASET.csv', sep=';')
        ciaa = df.loc[df['Venue'].isin(self.venue)]
        ciaa.to_csv(self.path+'data/cleaned/small_dataset.csv', index=False, sep=';')
    
    def create(self, small):
        self.create_structure()
        self.get_conference_sites()
        self.get_author_sites()
        self.get_publications()
        self.cleaning()
        if small: self.small_dataset()