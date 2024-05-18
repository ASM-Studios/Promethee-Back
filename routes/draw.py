from routes import routes, lobby_manager
from flask import Blueprint, jsonify, request
from LobbyManager import LobbyManager
from Player import Player
import sys
from Card import Card

@routes.route('/draw', methods=['GET'])
def draw_card():
    value = Card.generateRandom()
    return jsonify({"value": value}), 200
