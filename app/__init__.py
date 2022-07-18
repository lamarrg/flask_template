import os

from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__)
    
    # app.config.from_pyfile(<filename>)
    app.config.from_pyfile('settings.py')


    # a simple page that says hello, which will eventually be moved when blueprints are included
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app

    