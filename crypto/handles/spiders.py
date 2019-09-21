import subprocess
import os

def executeSpider(spider_name, coin_name=""):
    spider_path = 'crawlers/{}.py'.format(spider_name)
    outputs = ['scrapy', 'runspider', spider_path, '-o', 'output.json' ,'-s', 'HTTPCACHE_ENABLED=1']
    if coin_name != "":
        outputs.append('-a')
        outputs.append("crypto_coin={}".format(coin_name))

    try:
        subprocess.check_output(outputs)
        with open('output.json') as items_file:
            items = items_file.read()
            os.remove('output.json')
            if items == []:
                return 'The list is empty', 200
            else:
                return items,  200

    except EOFError:
        return 'Scrapy error', 500