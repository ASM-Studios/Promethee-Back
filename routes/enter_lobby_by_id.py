from flask import Blueprint, jsonify, request
from lobby.Player import Player
from lobby.LobbyManager import lobby_manager
import sys

enter_lobby_by_id_routes = Blueprint('enter_lobby_by_id', __name__)

@enter_lobby_by_id_routes.route('/enter_lobby_by_id', methods=['POST'])
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
        new_lobby.setCurrent(player)
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