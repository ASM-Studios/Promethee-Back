import random

from flask import Blueprint, jsonify, request

from lobby import questions
from lobby.LobbyManager import lobby_manager

question_routes = Blueprint('questions', __name__)

@question_routes.route('/question', methods=['PUT'])
def choose_question():
    data = request.get_json()
    lobby_id = data.get('lobbyId')
    username = data.get('username')

    for lobby in lobby_manager.get_lobbies():
        if lobby.getUUID() == lobby_id:
            player = lobby.getPlayer(username)
            if player:
                player.setAsGamble(True)

    question_id = random.randint(0, len(questions) - 1)
    return jsonify({
        "title": questions[question_id]["question"],
        "expected": questions[question_id]["expected"],
        "min": questions[question_id]["min"],
        "max": questions[question_id]["max"],
        "tolerance": questions[question_id]["tolerance"]
    }), 200
