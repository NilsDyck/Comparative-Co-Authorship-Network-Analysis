#Does not work yet!

import urllib.request, urllib.error, urllib.parse

class Download:

    def __init__(self, url):
        self.url = url
    def proceed():
        response = urllib.request.urlopen(url)
        return response.read().decode('UTF-8')