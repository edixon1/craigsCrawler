from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class ad(object):
    def __init__(self, title, location, date, price, photo, url):
        self.title = title
        self.location = location
        self.date = date
        self.price = price
        self.photo = photo
        self.url = url

class CraigslistScraper(object):
    def __init__(self, location, postal, max_price,radius):
        self.location = location
        self.postal = postal
        self.max_price = max_price
        self.radius = radius
        self.url = f"https://{location}.craigslist.org/search/sss?search_distance={radius}&postal={postal}&max_price={max_price}"
        
        html = urlopen(self.url)
        self.bs = BeautifulSoup(html.read(),'html.parser')
        
    def get_bs(self):
        return self.bs

    def get_ad_titles(self):
        results = self.bs.select('a.result-title')
        ad_titles = []
        for result in results:
            ad_titles.append(result.text)
        return ad_titles


    def get_ad_locations(self):
        results = self.bs.select("span.result-meta")
        ad_locations = []
        for result in results:
            ad_locations.append(result.select("span.result-hood"))
        return ad_locations


    def get_ad_prices(self):
        results = self.bs.select("span.result-meta>span.result-price")
        ad_prices = []
        for result in results:
            ad_prices.append(result.text)
        return ad_prices

    def get_ad_dates(self):
        pass

    def get_url(self):
        return self.url

    def get_ad_photos(self):
        results = self.bs.select('li.result-row>a')
        img_urls = []
        for result in results:
            if result.has_attr('data-ids'):
                img_id = result['data-ids']
                img_urls.append(f"http://images.craigslist.org/{img_id[2:19]}_300x300.jpg")
            else:
                img_urls.append("no image")
        return img_urls
    
    def get_ad_urls(self):
        ad_urls = []
        for line in self.bs.select('li.result-row>a'):
            ad_urls.append(line['href'])
        return ad_urls
        
            
        
location = "asheville"
postal = "28801"
max_price = "500"
radius = "5"    
scraper = CraigslistScraper(location,postal,max_price,radius)



titles = scraper.get_ad_titles()
prices = scraper.get_ad_prices()
for i in range(120):
    print(f"Title: {titles[i]}  \nprice: {prices[i]}\n\n")

print(len(titles))
print(len(prices))
print(scraper.get_url())
#print(scraper.get_ad_titles())
#print("\n------------------------------------\n")
#print(scraper.get_ad_prices())



# photos = scraper.get_ad_photos()
# titles = scraper.get_ad_titles()
# print(photos)

#page_photos = scraper.get_photos()