import subprocess
from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def api_status():
    return 'API is on and running!', 200

@app.route('/cryptocoins')
def get_coins():
    spider_name_path = "crawlers/crypto.py"
    return executeSpider(spider_name_path)

@app.route('/cryptocoins/<string:coin>')
def get_coin(coin):
    spider_name_path = "crawlers/crypto.py"
    return executeSpider(spider_name_path, coin.lower())


def executeSpider(spider_path, coin_name=""):
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

if __name__ == '__main__':
    app.run(debug=True)