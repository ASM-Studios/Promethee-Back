#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
import random
from question import questions
from Player import Player
from Lobby import Lobby
from LobbyManager import LobbyManager

app = Flask(__name__)

lobbyManager = LobbyManager()

@app.route('/', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = request.form['correct_answer']
        if user_answer == correct_answer:
            return redirect(url_for('quiz'))
        else:
            return "Wrong answer! Try again."
    question = random.choice(questions)
    return render_template('quiz.html', question=question)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
