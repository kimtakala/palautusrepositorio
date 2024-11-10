'importing the necessities'
import requests
from player import Player

def main():
    'main function'
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = []
    # "name":"Nils Lundkvist",
    # "nationality":"SWE",
    # "assists":17,
    # "goals":2,
    # "team":"DAL",
    # "games":59,
    # "id":8480878

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == 'FIN':
            players.append(player)

    print('Players from Finland')

    for player in players:
        print(f"""\
 {player.name:<20}\
 {player.team:<4}\
 {player.goals:<2} +\
 {player.assists:<2} =\
 {player.goals + player.assists}\
""")

if __name__ == "__main__":
    main()

    # Players from FIN

    # Mikko Rantanen       COL  55 + 50 = 105
    # Aleksander Barkov    FLA  23 + 55 = 78
    # Roope Hintz          DAL  37 + 38 = 75
