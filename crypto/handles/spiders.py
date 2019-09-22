"""This Module contains all methods that handle with spider from scrapy"""

import subprocess
import os

def execute_spider(spider_name, coin_name=""):
    """Methods that executes a specific spider

    This method returns a list of items scraped from
    coinMarketCap site.

    Parameters:
        - spider_name: Represents the name of a
    specific spider to execute
        - coin_name: If specified, the crawler returns
    informations only about this cryptocoin
    """
    spider_path = 'crawlers/{}.py'.format(spider_name)
    outputs = ['scrapy', 'runspider', spider_path, '-o', 'output.json']
    if coin_name != "":
        outputs.append('-a')
        outputs.append("crypto_coin={}".format(coin_name))

    try:
        subprocess.check_output(outputs)
        with open('output.json') as items_file:
            items = items_file.read()
            os.remove('output.json')
            if items == "":
                return 'The list does not contains this coin', 200
            return items, 200

    except EOFError:
        return 'Scrapy error', 500
