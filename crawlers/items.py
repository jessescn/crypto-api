import scrapy

class CoinItem(scrapy.Item):
    name= scrapy.Field()
    symbol=scrapy.Field()
    market_cap=scrapy.Field()
    price=scrapy.Field()
    circulation_supply=scrapy.Field()
    volume=scrapy.Field()
