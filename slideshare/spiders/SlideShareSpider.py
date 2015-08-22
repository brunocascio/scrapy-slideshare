from scrapy.spiders import Spider
from slideshare.items import SlideshareItem

class SlideShareSpider(Spider):
    name = 'SlideShareSpider'
    allowed_domains = ['es.slideshare.net', 'image.slidesharecdn.com']

    def __init__(self, url=''):
        self.start_urls = [ "%s" % url ]

    def parse(self, response):
        items = []
        for url in response.css('section img::attr("data-full")'):
            item = SlideshareItem()
            item['image_url'] = url.extract()
            items.append(item)
        return items
