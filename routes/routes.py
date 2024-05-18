from flask import Blueprint
from routes import *

routes = Blueprint('routes', __name__)
routes.register(question_routes)
routes.register(play_card_routes)
routes.register(enter_lobby_by_id_routes)
routes.register(draw_routes)

@routes.route('/ping', methods=['GET'])
def ping():
    return '', 200