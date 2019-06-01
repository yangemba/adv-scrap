import scrapy


class MySpider(scrapy.Spider):
    name = 'lofa'
    allowed_domains = ['example.com']
    start_urls = [f'https://premier.ua/zhilaia-nedvizhimost/prodazha-1-komn-kv-?page={x}' for x in range(400)]

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)


