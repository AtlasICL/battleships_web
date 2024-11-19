from flask import Flask, render_template, jsonify, request

import components

app = Flask(__name__)


@app.route('/', methods=['GET'])
def render_main():
    board = components.initialise_board()
    board = components.place_battleships(board, components.create_battleships(), "custom")
    return render_template('main.html', player_board=board)


@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    if request.method == 'POST':
        data = request.get_json()
        return jsonify({'message': 'Received'}), 200

    ships_in_play = components.create_battleships()
    return render_template('placement.html', ships=ships_in_play, board_size=10)


@app.route('/attack', methods=['GET'])
def attack():
    return "some_function2"



if __name__ == "__main__":
    app.run()


