from flask import Blueprint, jsonify, request
from lobby import lobby_manager

play_card_routes = Blueprint('play_card', __name__)

@play_card_routes.route('/play_card', methods=['POST'])
def play_card():
    data = request.get_json()
    lobby_id = data.get('lobbyId')
    username = data.get('username')
    value = data.get('value')
    action = data.get('action')
    target = data.get('target')
    target_player = None

    # Find the lobby
    for lobby in lobby_manager.get_lobbies():
        if lobby.getUUID() == lobby_id:
            break
    else:
        return jsonify({"error": "Lobby not found"}), 400

    # Check if the player is in the lobby
    player = lobby.getPlayer(username)
    if player is None:
        return jsonify({"error": "Player not found"}), 400

    # Find the target player
    if target is not None and target != "":
        target_player = lobby.getPlayer(target)
        if target_player is None:
            return jsonify({"error": "Target not found"}), 400

    # Apply the card
    if action == 'heal':
        if target is None or target == "":
            player.setLife(player.getLife() + value)
        else:
            target_player.setLife(target_player.getLife() + value)
    elif action == 'damage':
        if target is None or target == "":
            player.setLife(player.getLife() - value)
        else:
            target_player.setLife(target_player.getLife() - value)
    else:
        return jsonify({"error": "Invalid action"}), 400

    return '', 200
