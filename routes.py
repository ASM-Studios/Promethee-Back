import sys
import random
from flask import Blueprint, jsonify, request
from Lobby import Lobby
from LobbyManager import LobbyManager
from Player import Player
import random
from question import questions
from Card import Card

routes = Blueprint('routes', __name__)

lobby_manager = LobbyManager()


@routes.route('/ping', methods=['GET'])
def ping():
    return '', 200


@routes.route('/enter_lobby_by_id', methods=['POST'])
def enter_lobby_by_id():
    data = request.get_json()
    lobbyId = data.get('lobbyId')
    username = data.get('username')

    player = Player(username)

    if lobbyId:
        for lobby in lobby_manager.get_lobbies():
            if lobby.getUUID() == lobbyId:
                for p in lobby.getUsers():
                    print(p.getName(), file=sys.stderr)
                    if p.getName() == player.getName():
                        return jsonify({"error": "Username is already taken"}), 400
                try:
                    lobby.addUser(player)
                    return jsonify({
                        "lobbyId": lobbyId,
                        "creator": lobby.getCreator(),
                        "players": lobby.getPlayers()
                    })
                except Exception as e:
                    return jsonify({"error": str(e)}), 400

        # Create a new lobby if it doesn't exist
        new_lobby = lobby_manager.createLobby(lobbyId)
        new_lobby.addUser(player)
        new_lobby.addCreator(player.getName())
        lobby_manager.get_lobbies().append(new_lobby)
        return jsonify({
            "lobbyId": new_lobby.getUUID(),
            "creator": player.getName(),
            "players": [{"username": player.getName(), "life": player.getLife()}]
        })
    for lobby in lobby_manager.get_lobbies():
        print(lobby.getUUID(), file=sys.stderr)
        for player in lobby.getPlayers():
            print(player.getName(), file=sys.stderr)
    return '', 200


@routes.route('/play_card', methods=['POST'])
def play_card():
    data = request.get_json()
    lobbyId = data.get('lobbyId')
    username = data.get('username')
    value = data.get('value')
    action = data.get('action')
    target = data.get('target')

    # Find the lobby
    for lobby in lobby_manager.get_lobbies():
        if lobby.getUUID() == lobbyId:
            break
    else:
        return jsonify({"error": "Lobby not found"}), 400

    # Find the player and target
    player = None
    target_player = None
    for player_ in lobby.getPlayers():
        if player_.getName() == username:
            player = player_
        if player_.getName() == target:
            target_player = player_
    if not player:
        return jsonify({"error": "Player not found"}), 400
    if not target_player and target is not None:
        return jsonify({"error": "Target not found"}), 400

    # Apply the card
    if action == 'heal':
        if target is None:
            player.setLife(player.getLife() + value)
        else:
            target_player.setLife(target_player.getLife() + value)
    elif action == 'damage':
        if target is None:
            player.setLife(player.getLife() - value)
        else:
            target_player.setLife(target_player.getLife() - value)
    else:
        return jsonify({"error": "Invalid action"}), 400

    return '', 200

@routes.route('/question', methods=['GET'])
def choose_question():
    question_id = random.randint(0, len(questions) - 1)
    return jsonify({
        "question": questions[question_id]["question"],
        "expected": questions[question_id]["expected"],
        "min": questions[question_id]["min"],
        "max": questions[question_id]["max"],
        "tolerance": questions[question_id]["tolerance"]
    })

@routes.route('/draw', methods=['GET'])
def draw_card():
    value = Card.generateRandom()
    return jsonify({"value": value}), 200
