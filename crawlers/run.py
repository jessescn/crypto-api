from scrapy.crawler import CrawlerProcess
from crawlers.crypto import CryptoSpider

CONFIGS = {
        'LOG_ENABLED':False
}

def scrapy_coins(coin_name=""):
    """Método que executa o crawler de coins"""
    process = CrawlerProcess(settings=CONFIGS)
    process.crawl(CryptoSpider, coin_name)
    process.start()
    return CryptoSpider.items
