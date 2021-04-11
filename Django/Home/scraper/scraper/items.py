# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from itnews.models import IT_news
from economy.models import EconomyNews

class IT_Item(DjangoItem):

    django_model = IT_news

class EconomyItem(DjangoItem):
    django_model = EconomyNews



    