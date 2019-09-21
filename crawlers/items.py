"""This Module contains all classes that represents an element scraped"""
import scrapy

class CoinItem(scrapy.Item):
    """This class represents a coin scraped from coinMarketCap site"""
    name = scrapy.Field()
    symbol = scrapy.Field()
    market_cap = scrapy.Field()
    price = scrapy.Field()
    circulation_supply = scrapy.Field()
    volume = scrapy.Field()
