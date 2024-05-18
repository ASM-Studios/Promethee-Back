#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS

from routes.routes import routes

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = '*'
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)