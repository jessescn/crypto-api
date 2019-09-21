# -*- coding: utf-8 -*-
import scrapy
from crawlers.items import CoinItem

class CryptoSpider(scrapy.Spider):
    """Spider para raspar os dados das cryptomoedas"""

    name = 'crypto'
    start_urls = ['https://coinmarketcap.com/all/views/all/']
    items = []

    def __init__(self, crypto_coin):
        self.crypto_coin = crypto_coin

    def start_requests(self):
        """Faz as requisições para as URLs  na lista dos 'start_urls"""
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        """Callback para raspagem dos dados

        Método que recebe o html e faz a ras-
        pagem dos dados das cryptomoedas,
        caso o valor da variável 'crypto_coin'
        for diferente de "", a raspagem é espe-
        cificada a partir dessa moeda
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

            self.items.append(coin)

            yield coin
