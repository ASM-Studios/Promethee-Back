from .play_card import routes as play_card_routes
from .question import routes as question_routes
from .enter_lobby_by_id import routes as enter_lobby_by_id_routes
from .draw import routes as draw_routes

from lobby.LobbyManager import LobbyManager

lobby_manager = LobbyManager()