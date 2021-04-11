import scrapy
from scrapy.http import Request
from scraper.items import IT_Item

URL = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=105&page=%s'
page_num = 1

class ItSpider(scrapy.Spider):
    name = 'IT'
    allowed_domains = ['naver.com']
    start_urls = [URL % page_num]

    def start_requests(self):
        for i in range(5): 
            yield Request(url= URL % (i + page_num), callback=self.parse)

    def parse(self, response):
        titles = response.xpath('//*[@id="main_content"]/div[2]/ul/li/dl/dt[last()]/a/text()').extract()
        summarys = response.css('.lede::text').extract()
        papers = response.css('.writing::text').extract()

        for row in zip(titles, summarys, papers):
            item = IT_Item()
            item['title'] = row[0].strip()
            item['summary'] = row[1]
            item['paper'] = row[2]

            yield item
