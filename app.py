import json
import requests

BASE_URL = "selected-ardelle-cassiano-flores-5f46ffab.koyeb.app"


def get_players():
    response = requests.get(f"{BASE_URL}/players")
    if response.status_code == 200:
        players = response.json()
        print(json.dumps(players, indent=4))
    else:
        print("Erro ao obter jogadores")


def get_player(player_id):
    response = requests.get(f"{BASE_URL}/player/{player_id}")
    if response.status_code == 200:
        player = response.json()
        print(json.dumps(player, indent=4))
    else:
        print("Erro ao obter jogador")


def update_player(player_id, player_data):
    response = requests.put(f"{BASE_URL}/player/{player_id}", json=player_data)
    if response.status_code == 200:
        player = response.json()
        print(json.dumps(player, indent=4))
    else:
        print("Erro ao atualizar jogador")


def add_player(player_data):
    response = requests.post(f"{BASE_URL}/player", json=player_data)
    if response.status_code == 200:
        player = response.json()
        print(json.dumps(player, indent=4))
    else:
        print("Erro ao adicionar jogador")


def remove_player(player_id):
    response = requests.delete(f"{BASE_URL}/player/{player_id}")
    if response.status_code == 200:
        print(f"Jogador com ID {player_id} foi deletado")
    else:
        print("Erro ao remover jogador")


def main():
    while True:
        print("\nEscolha uma opção:")
        print("1. Obter todos os jogadores")
        print("2. Obter jogador por ID")
        print("3. Atualizar jogador")
        print("4. Adicionar jogador")
        print("5. Remover jogador")
        print("6. Sair")

        choice = input("Digite o número da opção: ")

        if choice == "1":
            get_players()
        elif choice == "2":
            player_id = int(input("Digite o ID do jogador: "))
            get_player(player_id)
        elif choice == "3":
            player_id = int(input("Digite o ID do jogador: "))
            player_data = json.loads(input("Digite os dados do jogador em JSON: "))
            update_player(player_id, player_data)
        elif choice == "4":
            player_data = json.loads(input("Digite os dados do jogador em JSON: "))
            add_player(player_data)
        elif choice == "5":
            player_id = int(input("Digite o ID do jogador: "))
            remove_player(player_id)
        elif choice == "6":
            break
        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
