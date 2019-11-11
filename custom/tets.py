import bs4
import requests
import logging


class MySpider(object):

    def __init__(self, **kwargs):
        self.link = kwargs.get('link')

    def get_residential_list(self):
        residential_estate_body = requests.get(self.link).text
        soup = bs4.BeautifulSoup(residential_estate_body, 'html.parser')
        return soup

    def print_l(self):
        soup = self.get_residential_list()
        list_link = [f"https://premier.ua/{x.attrs['href']}" for x in
                     soup.select('.catlist a')]
        return list_link


a = MySpider(link='https://premier.ua/zhilaia-nedvizhimost' )
b = a.print_l()

list_links = []

for el in b:
    a = MySpider(link=el)
    b = a.print_l()
    list_links += b

logging.warning(f'qnt - {len(list_links)}')

394