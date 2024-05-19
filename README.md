# Project Title

A brief description of what this project does and who it's for.

## Installation

Instructions on how to install the project or setup the development environment.

### Requirements

- Python 3.8
- Pip

Create a python venv and activate it:
```bash
python3 -m venv .venv
source venv/bin/activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Instructions on how to use the project after installation.

### Running the server

To run the server, you need to set the PYTHONPATH environment variable to the project directory:
```bash
export PYTHONPATH="${PYTHONPATH}:/path/to/project"
```

Then, run the following command to start the server:
```bash
flask run --host=localhost --port=8080
```

## Routes

GET /ping
    Check if the server is running.

GET /draw
    Draw a random card from a deck.

PUT /end_of_turn
    End the current turn. switch to the next player.

POST /enter_lobby_by_id
    Join or create a lobby by id.

POST /play_card
    Play a card from the player's hand.

PUT /question
    Ask a question to the player.

PUT /update
    get the current state of the game.

## Frontend

The frontend of the project is a Vite.js React application.
You can find the repository [here](https://github.com/ASM-Studios/Promethee-Front).

## Authors

- [Charles MADJERI](charles.madjeri@epitech.eu)
- [Mathieu Borel](mathieu.borel@epitech.eu)
- [Yohann Mangenot](yohann.mangenot@epitech.eu)
- [Tom Blancheton](tom.blancheton@epitech.eu)
- [Mathieu Coulet](mathieu.coulet@epitech.eu)
- [Mael RABOT](mael.rabot@epitech.eu)
