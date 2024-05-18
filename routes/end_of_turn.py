from flask import Blueprint, request, jsonify
from lobby.LobbyManager import lobby_manager

EOT_routes = Blueprint('EOT_routes', __name__)


@EOT_routes.route('/end_of_turn', methods=['PUT'])
def end_of_turn():
    data = request.get_json()
    lobbyId = data.get('lobbyId')
    for lobby in lobby_manager.get_lobbies():
        if lobby.getUUID() == lobbyId:
            break
    else:
        return jsonify({"error": "Lobby not found"}), 400
    player = lobby.getNext()
    return jsonify({
        "username": player.getName()
    })

