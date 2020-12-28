import scrapy
from scrapy.spiders import CrawlSpider, Rule
from ..items import JobscraperItem
from scrapy.linkextractors import LinkExtractor



class JobscraperSpider(CrawlSpider):
    name ='jobspider'
    start_urls = ['https://mott.pe/bolsa/ofertas?oferta=&lugar=&categoria=']

    rules = (

        Rule(LinkExtractor(allow=('/bolsa/16',)), follow=True, callback='parse_item'),

    )

    def parse_item(self, response):
        items = JobscraperItem()

        job_title = response.xpath('//h1/text()').extract_first()
        company = response.xpath('//h2/b/text()').extract_first()
        company_url = response.xpath('//div[@class="pull-left"]/a/text()').extract_first()
        description = response.xpath('string(//div[@class="aviso"])').extract_first().strip()
        salary = response.xpath('//div[@id="aviso"]/p[1]/text()').extract_first()
        city = response.xpath('//div[@id="aviso"]/p[2]/text()').extract_first()
        district = response.xpath('//div[@id="aviso"]/p[5]/text()').extract_first()
        publication_date = response.xpath('//div[@class="fecha"]/text()').extract_first()
        job_url = response.url
        job_type = response.xpath('//div[@id="resumen"]/p[3]/text()').extract_first()

        items['job_title'] = job_title
        items['company'] = company
        items['company_url'] = company_url
        items['description'] = description
        items['salary'] = salary
        items['city'] = city
        items['district'] = district
        items['publication_date'] = publication_date
        items['job_url'] = job_url
        items['job_type'] = job_type
        #items['apply'] = apply

        yield items
