"""This Module contains a blueprint with routes"""
from flask import Blueprint
from crypto.handles.spiders import execute_spider

datasets = Blueprint('datasets', __name__)

@datasets.route('/crypto', methods=['GET'], strict_slashes=False)
def get_coins():
    """Method that returns a list with data about all cryptocoins"""
    spider_name = "crypto"
    return execute_spider(spider_name)

@datasets.route('/crypto/<string:name>', methods=['GET'], strict_slashes=False)
def get_coin(name):
    """Method that returns a list with data about an especific cryptocoin"""
    spider_name = "crypto"
    return execute_spider(spider_name, name.lower())
