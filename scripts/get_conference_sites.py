#   download CIAA conferences sites from DBLP
#   Nils Dyck, 28.04.2023

import urllib.request, urllib.error, urllib.parse, webbrowser

#As the urls from the conferences are pretty similliar, we compute them with a loop
urls = ['https://dblp.uni-trier.de/db/conf/dcfs/dcfs'+str(i)+'.html' for i in range(2001,2023)]
# urls = ['https://dblp.uni-trier.de/db/conf/wia/wia'+str(i)+'.html' if i<2000 else 'https://dblp.uni-trier.de/db/conf/wia/ciaa'+str(i)+'.html' for i in range(1996,2023)]


#cook the soup for every url and save the html-code into the correct file
# year = 1996
year = 2001
for url in urls:
    # CIAA code
    
    #the following code is a little acrobatic but the urls from 2009 and 2010 are not matching the pattern and this was my straightforward solution
    # if year != 2020:
    #     response = urllib.request.urlopen(url)
    #     webContent = response.read().decode('UTF-8')
    #     with open('data/raw/CIAA/ciaa'+str(year)+'.html', 'w') as f:
    #         f.write(repr(webContent))
    #     print(url)
    #     print(year)
    
    # DCFS code
    if year != 2009 and year != 2010:
        response = urllib.request.urlopen(url)
        webContent = response.read().decode('UTF-8')
        with open('data/raw/DCFS/dcfs'+str(year)+'.html', 'w') as f:
            f.write(repr(webContent))
    elif year == 2009: 
        response = urllib.request.urlopen('https://dblp.uni-trier.de/db/series/eptcs/eptcs3.html')
        webContent = response.read().decode('UTF-8')
        with open('data/raw/DCFS/dcfs'+str(year)+'.html', 'w') as f:
            f.write(repr(webContent))
    else:
        response = urllib.request.urlopen('https://dblp.uni-trier.de/db/series/eptcs/eptcs31.html')
        webContent = response.read().decode('UTF-8')
        with open('data/raw/DCFS/dcfs'+str(year)+'.html', 'w') as f:
            f.write(repr(webContent))

    year += 1

for url in urls:
    webbrowser.open(url)

