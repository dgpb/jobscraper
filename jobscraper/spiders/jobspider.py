import scrapy
from ..items import JobscraperItem
from scrapy.linkextractors import LinkExtractor



class JobscraperSpider(scrapy.Spider):
    name ='jobspider'
    start_urls = ['https://mott.pe/bolsa/ofertas?oferta=&lugar=&categoria=']

    def parse(self, response):
        job_detail = response.xpath('//div[@class="list"]/div/a')
        yield from response.follow_all(job_detail, self.parse_jobspider)

    def parse(self, response):
        items = JobscraperItem()

        job_title = response.xpath('//h1/text()').extract()
        company = response.xpath('//h2/b/text()').extract()
        company_url = response.xpath('//div[@class="pull-left"]/a/text()').extract()
        description = response.xpath('//div[@class="aviso"]/text()').extract()
        salary = response.xpath('//div[@id="aviso"]/p[1]/text()').extract()
        city = response.xpath('//div[@id="aviso"]/p[2]/text()').extract()
        district = response.xpath('//div[@id="aviso"]/p[5]/text()').extract()
        publication_date = response.xpath('//div[@id="publicado"]/text()').extract()
        apply = response.xpath('//p[@class="text-center"]/b/text()').extract()
        job_type = response.xpath('//div[@id="resumen"]/p[3]/text()').extract()

        items['job_title'] = job_title
        items['company'] = company
        items['company_url'] = company_url
        items['description'] = description
        items['salary'] = salary
        items['city'] = city
        items['district'] = district
        items['publication_date'] = publication_date
        items['apply'] = apply
        items['job_type'] = job_type

        yield items
