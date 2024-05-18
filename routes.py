from flask import Blueprint, jsonify, request
from flask_cors import CORS, cross_origin
from Lobby import Lobby, LobbyManager
from Player import Player

routes = Blueprint('routes', __name__)

lobby_manager = LobbyManager()


@routes.route('/ping', methods=['GET'])
@cross_origin()
def ping():
    return '', 200


@routes.route('/enter_lobby_by_id', methods=['POST'])
@cross_origin()
def enter_lobby_by_id():
    data = request.get_json()
    lobbyId = data.get('lobbyId')  # changed to camelCase
    username = data.get('username')

    player = Player(username)

    if lobbyId:
        for lobby in lobby_manager.get_lobbies():
            if lobby.getUUID() == lobbyId:
                try:
                    lobby.addUser(player)
                    return jsonify({
                        "lobbyId": lobbyId,  # changed to camelCase
                        "creator": lobby.getPlayers()[0].getName(),
                        "users": [player.getName() for player in lobby.getPlayers()]
                    })
                except Exception as e:
                    return jsonify({"error": str(e)}), 400

        # Create a new lobby if it doesn't exist
        new_lobby = Lobby(lobbyId)
        new_lobby.addUser(player)
        lobby_manager.get_lobbies().append(new_lobby)
        return jsonify({
            "lobbyId": new_lobby.getUUID(),  # changed to camelCase
            "creator": player.getName(),
            "users": [player.getName()]
        })
    else:
        # Create a new lobby with a random UUID
        new_lobby = Lobby(None)
        new_lobby.addUser(player)
        lobby_manager.get_lobbies().append(new_lobby)
        return jsonify({
            "lobbyId": new_lobby.getUUID(),  # changed to camelCase
            "creator": player.getName(),
            "users": [player.getName()]
        })


@routes.route('/play_card', methods=['POST'])
@cross_origin()
def play_card():
    data = request.get_json()
    lobbyId = data.get('lobbyId')  # changed to camelCase
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
