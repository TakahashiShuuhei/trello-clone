from flask import Flask, jsonify, request
from db import board

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return 'Hello'


@app.route('/api/v1/boards/<int:board_id>', methods=['GET'])
def get_board(board_id):
    return jsonify(board.get(board_id))


@app.route('/api/v1/boards', methods=['POST'])
def create_board():
    return jsonify(board.create(request.json))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
