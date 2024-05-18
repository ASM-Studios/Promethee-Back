from flask import Blueprint
from . import play_card_routes, question_routes, enter_lobby_by_id_routes, draw_routes, update_routes, EOT_routes

routes = Blueprint('routes', __name__)
routes.register_blueprint(play_card_routes)
routes.register_blueprint(question_routes)
routes.register_blueprint(enter_lobby_by_id_routes)
routes.register_blueprint(draw_routes)
routes.register_blueprint(update_routes)
routes.register_blueprint(EOT_routes)

@routes.route('/ping', methods=['GET'])
def ping():
    return '', 200