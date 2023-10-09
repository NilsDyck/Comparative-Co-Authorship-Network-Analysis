#   downloads the main site of CIAA at DBLP
#   Nils Dyck, 28.04.2023

import urllib.request, urllib.error, urllib.parse

# url = 'https://dblp.uni-trier.de/db/conf/wia/index.html'
url = 'https://dblp.uni-trier.de/db/conf/dcfs/index.html'

#download html code and save to string called webContent
response = urllib.request.urlopen(url)
webContent = response.read().decode('UTF-8')

with open('data/raw/DBLP-DCFS-main_site.html', 'w') as f:
    f.write(webContent)