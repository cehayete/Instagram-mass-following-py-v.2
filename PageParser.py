from urllib import request
from bs4 import BeautifulSoup
import json
import certifi

# This parser gets username instagram
# and  returns it 12 image, JSON data and user_id

class Parser:
    def __init__(self,username):
        self.username = username
        self.url = 'https://www.instagram.com/' + username
        self.html = None
        self.soup = None
        self.json = None
        self.images = []

    def getHtml(self):
        self.html = request.urlopen(self.url, cafile=certifi.where())
        return self.html

    def getSoup(self):
        self.getHtml()
        self.soup = BeautifulSoup(self.html,'html.parser')
        return self.soup

    def getJson(self):
        self.getSoup()
        scripts = self.soup.findAll('script', {'type':'text/javascript'})
        for script in scripts:
            if str(script).find('window._sharedData = ') > 0:
                self.json = json.loads(str(script.text).replace('window._sharedData = ','')[:-1])
                break
        return self.json

    def getImages(self):
        self.getJson()
        for img in self.json['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']:
            if str(img['node']['is_video']) == "False":
                self.images.append(img['node']['display_url'])
        return self.images

    def getUserId(self):
        self.json = self.getJson()
        try:
            return str(self.json['entry_data']['ProfilePage'][0]['logging_page_id']).replace('profilePage_', '')
        except:
            return

#  example
"""
p = Parser('sayonaraboy')

print('{0} have id: {1}\n'.format(p.username, p.getUserId()))
print('His 12 posts (Only photo):')
for img in p.getImages():
    print(img)

"""