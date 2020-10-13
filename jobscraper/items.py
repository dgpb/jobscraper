# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_title = scrapy.Field()
    company = scrapy.Field()
    company_url = scrapy.Field()
    description = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    publication_date = scrapy.Field()
    apply = scrapy.Field()
    job_type = scrapy.Field()

    pass
