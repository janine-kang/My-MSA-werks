# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
from itnews.models import IT_news
from economy.models import EconomyNews
from scrapy.exceptions import DropItem


class ScraperPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'IT':
            IT_news.objects.create(
                title = item['title'],
                summary = item['summary'],
                paper = item['paper']
            )
            return item

        else:
            EconomyNews.objects.create(
                title = item['title'],
                summary = item['summary'],
                paper = item['paper']
            )
            return item





