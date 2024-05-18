#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import random
from question import questions
from Player import Player
from Lobby import Lobby
from flask import Flask
from flask_cors import CORS, cross_origin
from routes import routes

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
