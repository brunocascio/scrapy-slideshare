# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
import slideshare.settings

class SlidesharePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['image_url'])

    def file_path(self, request, response=None, info=None):
        # Motherfucker, but works
        # get the slide number of slide
        image_guid = request.url.split('/')[-1].split('-')[-2]
        return 'full/%s' % (image_guid)

    def item_completed(self, results, item, info):
        return item
