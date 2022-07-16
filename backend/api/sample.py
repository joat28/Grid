from flask import jsonify, Blueprint

sample = Blueprint('sample', __name__,url_prefix='/sample')

def hello():
    return jsonify({'message': 'Hello, World! from sample'})

@sample.route('/test', methods=['GET'])
def get_sample():
    return hello()