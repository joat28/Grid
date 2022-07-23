import os
from flask import Flask
from flask_cors import CORS


from api.sample import sample as sampleblueprint
from api.twitter import twitter as twitterblueprint
from api.facebook import facebook as facebookblueprint
from api.instyle import instyle as instyleblueprint


def create_app():
    """
    FLask Appication
    """
    app = Flask(__name__)
    CORS(app)
    

    #api register
    app.register_blueprint(sampleblueprint)
    app.register_blueprint(twitterblueprint)
    app.register_blueprint(facebookblueprint)
    app.register_blueprint(instyleblueprint)

    return app
