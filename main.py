import pandas as pd
from flask import Flask, jsonify

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


# PUT
# POST
# DELETE


if __name__ == '__main__':
    app.run(debug=True)
