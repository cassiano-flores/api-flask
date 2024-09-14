import pandas as pd
from flask import Flask, jsonify, request

CSV_FILE = "nba_players.csv"
DATASET = pd.read_csv(CSV_FILE, sep=";")

app = Flask(__name__)


# GET - retorna todos os jogadores
@app.route('/players', methods=['GET'])
def get_players():
    players = DATASET.to_dict(orient="records")
    return jsonify(players), 200


# GET - retorna um jogador especifico pelo indice (ID)
@app.route('/player/<int:id>', methods=['GET'])
def get_player(id):
    if 0 <= id < len(DATASET):
        player = DATASET.iloc[id].to_dict()
        return jsonify(player), 200
    else:
        return jsonify({'message': 'Player not found'}), 404


# PUT - atualiza um jogador especifico pelo indice (ID)
@app.route('/player/<int:id>', methods=['PUT'])
def update_player(id):
    if 0 <= id < len(DATASET):
        new_data = request.json
        for key in new_data.keys():
            DATASET.at[id, key] = new_data[key]

        player = DATASET.iloc[id].to_dict()
        return jsonify(player), 200
    else:
        return jsonify({'message': 'Player not found'}), 404


# POST - adiciona novo jogador
@app.route('/player', methods=['POST'])
def add_player():
    global DATASET

    new_player = pd.DataFrame([request.json])
    DATASET = pd.concat([DATASET, new_player], ignore_index=True)

    player = DATASET.iloc[-1].to_dict()
    return jsonify(player), 200


# DELETE - remove um jogador especifico pelo indice (ID)
@app.route('/player/<int:id>', methods=['DELETE'])
def remove_player(id):
    global DATASET

    if 0 <= id < len(DATASET):
        DATASET = DATASET.drop(index=id).reset_index(drop=True)
        return jsonify({'message': f'Player with index {id} has been deleted.'}), 200
    else:
        return jsonify({'message': 'Player not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
