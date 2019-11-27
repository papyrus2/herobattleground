import os
import sys

from flask import Flask, jsonify
from flask import request, render_template
from flask import abort
from flask import make_response
from google.protobuf.json_format import MessageToDict

from clients.characters import CharactersClient
from clients.battleground import BattlegroundClient
from protos.python.battleground_pb2 import BattlegroundRequest

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    """ Handler 404 error in a better way """
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(error):
    """ Handler 400 error in a better way """
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.route('/character/', methods=['GET'])
def get_character():
    """
    Use GET method to get a battleground character
    """
    character_type = request.args.get('character_type')

    if character_type is None:
        abort(400, "Need to provide a character_type.")

    # get character
    client = CharactersClient()

    character = client.get({'character_type': character_type})

    return jsonify(MessageToDict(character))


@app.route('/battleground/', methods=['GET'])
def battleground():
    """
    Use GET method to get a random battleground
    """
    character_client = CharactersClient()
    human_player = character_client.get({'character_type': "HUMAN"}).character
    beast_player = character_client.get({'character_type': "BEAST"}).character

    battle_client = BattlegroundClient()

    battle = battle_client.fighting(BattlegroundRequest(first_player=human_player, second_player=beast_player))

    return render_template('battleground.html', battle=battle)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    print("Start flask server")
    app.run(host="0.0.0.0", port=5000, debug=True)