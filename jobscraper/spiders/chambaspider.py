import scrapy
from scrapy.spiders import CrawlSpider, Rule
from ..items import JobscraperItem
from scrapy.linkextractors import LinkExtractor



class JobscraperSpider(CrawlSpider):
    name ='chambaspider'
    start_urls = ['https://www.chambaparacreativos.com/bolsa-trabajo-postulantes/?page=1']

    rules = (

        Rule(LinkExtractor(allow=('/bolsa-trabajo-detalle/',)), follow=True, callback='parse_item'),

    )

    def parse_item(self, response):
        items = JobscraperItem()

        job_title = response.xpath('//div[@class="b10-puesto detail"]/h3/text()').extract_first()
        company = response.xpath('//div[@class="b10-puesto detail"]/span/text()').extract_first()
        #company_url = response.xpath('//div[@class="pull-left"]/a/text()').extract_first()
        description = response.xpath('string(//div[@class="b10-descrip"]/ul[1]/li[1]/span)').extract_first().strip()
        salary = response.xpath('//div[@class="b10-descrip"]/ul[2]/li[5]/span/text()').extract_first()
        #city = response.xpath('//div[@id="aviso"]/p[2]/text()').extract_first()
        #district = response.xpath('//div[@id="aviso"]/p[5]/text()').extract_first()
        #publication_date = response.xpath('//div[@class="fecha"]/text()').extract_first()
        job_url = response.url
        job_type = response.xpath('//div[@class="b10-descrip"]/ul[1]/li[3]/span/text()').extract_first()

        items['job_title'] = job_title
        items['company'] = company
        #items['company_url'] = company_url
        items['description'] = description
        items['salary'] = salary
        #items['city'] = city
        #items['district'] = district
        #items['publication_date'] = publication_date
        items['job_url'] = job_url
        items['job_type'] = job_type
        #items['apply'] = apply

        yield items
