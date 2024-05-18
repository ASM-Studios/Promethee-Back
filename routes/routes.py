import sys
import random
from flask import Blueprint, jsonify, request
from Lobby import Lobby
from LobbyManager import LobbyManager
from Player import Player
import random
from Card import Card

routes = Blueprint('routes', __name__)

lobby_manager = LobbyManager()

@routes.route('/ping', methods=['GET'])
def ping():
    return '', 200