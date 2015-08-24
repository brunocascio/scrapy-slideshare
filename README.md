# Scrapy Slideshare

Script for Slideshare scraping, using the python framework [scrapy](http://scrapy.org/).

## How to use

* Clone this repo:

    `git clone https://github.com/brunocascio/scrapy-slideshare && cd scrapy-slideshare`

* Install dependences:

   `chmod +x install.sh && sudo ./install.sh`

    **NOTE**: It works only in Debian like OS. Tested only in **Ubuntu 14.04**. Please consider contribute to this package for others installations. For more info [visit download page](http://scrapy.org/download/).

* Run the Spider :D

   `scrapy crawl SlideShareSpider -a url=<URL_OF_SLIDESHARE>`

* The images are downloaded in `images/<nameOfSlideShare>` folder on root directory.
