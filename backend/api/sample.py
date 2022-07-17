from flask import jsonify, Blueprint
from api.helper.categories import get_categories
sample = Blueprint('sample', __name__,url_prefix='/sample')

def hello():
    return get_categories()

@sample.route('/test', methods=['GET'])
def get_sample():
    return hello()