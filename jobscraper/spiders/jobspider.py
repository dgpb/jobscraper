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
        job_list = response.xpath('//div[@itemtype="http://schema.org/JobPosting"]')

        for job in job_list:
            item = JobscraperItem()

            job_title = job.xpath('//h1/text()').extract()
            company = job.xpath('//h2/b/text()').extract()
            company_url = job.xpath('//div[@class="pull-left"]/a/text()').extract()
            description = job.xpath('//div[@class="aviso"]/text()').extract()
            salary = job.xpath('//div[@id="aviso"]/p[1]/text()').extract()
            city = job.xpath('//div[@id="aviso"]/p[2]/text()').extract()
            district = job.xpath('//div[@id="aviso"]/p[5]/text()').extract()
            publication_date = job.xpath('//div[@id="publicado"]/text()').extract()
            apply = job.xpath('//p[@class="text-center"]/b/text()').extract()
            job_type = job.xpath('//div[@id="resumen"]/p[3]/text()').extract()

            item['job_title'] = job_title
            item['company'] = company
            item['company_url'] = company_url
            item['description'] = description
            item['salary'] = salary
            item['city'] = city
            item['district'] = district
            item['publication_date'] = publication_date
            item['apply'] = apply
            item['job_type'] = job_type

            yield item
