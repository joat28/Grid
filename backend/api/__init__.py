import os
from flask import Flask
from flask_cors import CORS


from api.sample import sample as sampleblueprint


def create_app():
    """
    FLask Appication
    """
    app = Flask(__name__)
    CORS(app)
    

    #api register
    app.register_blueprint(sampleblueprint)

    return app
