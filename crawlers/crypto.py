# -*- coding: utf-8 -*-
"""This Module contains a spider to  scrapy data about cryptocoins from coinMarketCap"""
import scrapy
from items import CoinItem

class CryptoSpider(scrapy.Spider):
    """Spider to scrapy data from coinMarketCap"""

    name = 'crypto'
    start_urls = ['https://coinmarketcap.com/all/views/all/']

    def __init__(self, crypto_coin=""):
        self.crypto_coin = crypto_coin

    def start_requests(self):
        """Method that makes requests to all URLs within start_urls"""
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        """Callback to scrapy data

       Method that receives an html and
       scrapy data about one or each
       cryptocoin inside the html
        """
        table = []

        if self.crypto_coin != "":
            table.append(response.css('#id-{}'.format(self.crypto_coin)))

        else:
            table = response.css("tbody tr")

        for row in table:
            coin = CoinItem(
                name=row.css("a.currency-name-container::text").get(),
                symbol=row.css("td.col-symbol::text").get(),
                market_cap=row.css("td.market-cap::text").get().replace('\n', ''),
                price=row.css("a.price::attr(data-usd)").get(),
                circulation_supply=row.css("td.circulating-supply span::attr(data-supply)").get(),
                volume=row.css("a.volume::attr(data-usd)").get())

            yield coin
