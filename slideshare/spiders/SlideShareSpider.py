from scrapy.spiders import Spider
from slideshare.items import SlideshareItem

class SlideShareSpider(Spider):
    name = 'SlideShareSpider'
    allowed_domains = ['*.slideshare.net', 'slideshare.net', 'image.slidesharecdn.com']

    def __init__(self, url=''):
        self.start_urls = [ "%s" % url ]

    def parse(self, response):
        items = []
        for slide in response.css('section.slide'):
            item = SlideshareItem()
            # get number of slide
            #item['name'] = slide.css("::attr('data-index')").extract().pop()
            # get url of full image
            item['image_url'] = slide.css("img::attr('data-full')").extract().pop()
            items.append(item)
        return items
