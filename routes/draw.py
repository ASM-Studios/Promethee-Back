from flask import Blueprint, jsonify
from lobby.Card import Card

routes = Blueprint('routes', __name__)

@routes.route('/draw', methods=['GET'])
def draw_card():
    value = Card.generateRandom()
    return jsonify({"value": value}), 200
