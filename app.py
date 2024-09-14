import json
import requests

BASE_URL = "https://selected-ardelle-cassiano-flores-5f46ffab.koyeb.app"


def get_players():
    try:
        response = requests.get(f"{BASE_URL}/players")
        players = response.json()
        print(json.dumps(players, indent=4))
    except Exception as e:
        print(f"Endpoint not found. {e.__str__()}")


def get_player(player_id):
    try:
        response = requests.get(f"{BASE_URL}/player/{player_id}")
        player = response.json()
        print(json.dumps(player, indent=4))
    except Exception as e:
        print(f"Endpoint not found. {e.__str__()}")


def update_player(player_id, player_data):
    try:
        response = requests.put(f"{BASE_URL}/player/{player_id}", json=player_data)
        player = response.json()
        print(json.dumps(player, indent=4))
    except Exception as e:
        print(f"Endpoint not found. {e.__str__()}")


def add_player(player_data):
    try:
        response = requests.post(f"{BASE_URL}/player", json=player_data)
        player = response.json()
        print(json.dumps(player, indent=4))
    except Exception as e:
        print(f"Endpoint not found. {e.__str__()}")


def remove_player(player_id):
    try:
        requests.delete(f"{BASE_URL}/player/{player_id}")
        print(f"Player with index {player_id} has been deleted.")
    except Exception as e:
        print(f"Endpoint not found. {e.__str__()}")


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
