from flask import Blueprint, jsonify
from lobby.Card import Card

draw_routes = Blueprint('draw', __name__)

@draw_routes.route('/draw', methods=['GET'])
def draw_card():
    value = Card.generateRandom()
    return jsonify({"value": value}), 200
