from flask import Blueprint 
from crypto.handles.spiders import executeSpider

datasets = Blueprint('datasets', __name__)

@datasets.route('/cryptocoins', methods=['GET'], strict_slashes=False)
def get_coins():
    spider_name = "crypto"
    return executeSpider(spider_name)

@datasets.route('/cryptocoins/<string:name>', methods=['GET'], strict_slashes=False)
def get_coin(name):
    spider_name = "crypto"
    return executeSpider(spider_name, name.lower())


