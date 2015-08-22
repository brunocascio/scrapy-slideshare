# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import sys

if len(sys.argv) < 3:
    print "You must specify the url of Slideshare"
    print "Example: "
    print "scrapy crawl <spiderName> <url>"
    sys.exit(1)
