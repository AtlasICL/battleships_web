from flask import Flask, render_template, jsonify, request

import components, game_engine, mp_game_engine

app = Flask(__name__)

players = {}
players = mp_game_engine.initialise_players_dict()

all_user_ships_sunk: bool = False
all_ai_ships_sunk: bool = False

battleships = components.create_battleships()

@app.route('/', methods=['GET'])
def render_main():
    return render_template('main.html', player_board=players['user']['board'])


@app.route('/placement', methods=['GET', 'POST'])
def placement_interface():
    if request.method == 'POST':
        user_ship_placement_data = request.get_json()
        players["user"]["board"] = components.make_custom_board_from_json(user_ship_placement_data)
        return jsonify({'message': 'Received'}), 200

    global battleships
    return render_template('placement.html', ships=battleships, board_size=10)


@app.route('/attack', methods=['GET'])
def attack():

    # fetching user input coordinates
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))

    
    global players

    all_user_ships_sunk = game_engine.is_all_ships_sunk(players["user"]["ships"])
    all_ai_ships_sunk = game_engine.is_all_ships_sunk(players["ai"]["ships"])

    if not all_user_ships_sunk and not all_ai_ships_sunk:
        hit_success = game_engine.attack((x, y), players["ai"]["board"], players["ai"]["ships"])
        ai_attack = mp_game_engine.generate_attack(players["user"]["board"])

        return jsonify({'hit': hit_success,
            'AI_Turn': ai_attack,
            'finished': "NEXT TURN"
            })
    
    return jsonify({'hit': False,
        'AI_Turn': (0,0),
        'finished': "PLAYER WINS" if all_ai_ships_sunk else "AI WINS"
        })
    



if __name__ == "__main__":
    app.run()


