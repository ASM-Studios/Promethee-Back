from flask import Blueprint, jsonify
import random
from lobby import *

routes = Blueprint('routes', __name__)

@routes.route('/question', methods=['GET'])
def choose_question():
    question_id = random.randint(0, len(questions) - 1)
    return jsonify({
        "question": questions[question_id]["question"],
        "expected": questions[question_id]["expected"],
        "min": questions[question_id]["min"],
        "max": questions[question_id]["max"],
        "tolerance": questions[question_id]["tolerance"]
    }), 200
