import scrapy
import bs4
import requests

class MySpider(scrapy.Spider):
    # name = 'lofa'
    # allowed_domains = ['example.com']
    # start_urls = [f'https://premier.ua/zhilaia-nedvizhimost/prodazha-1-komn-kv-?page={x}' for x in range(400)]

    @staticmethod
    def get_residential_list():
        residential_estate_body = requests.get("https://premier.ua/zhilaia-nedvizhimost").text
        soup = bs4.BeautifulSoup(residential_estate_body, 'html.parser')
        return soup

    soup = get_residential_list()
    list = [f"https://premier.ua/{x.attrs['href']}" for x in soup.xpath('//*[@id="category0"]/table)')]

    def parse_category(self, response):
        for category in #category0 > table


