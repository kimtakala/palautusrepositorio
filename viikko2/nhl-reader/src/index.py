'importing the necessities'
import requests
from player import Player

class PlayerReader():
    'reading the players from json and transforming them into classes'
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        'getting players'
        # "name":"Nils Lundkvist",
        # "nationality":"SWE",
        # "assists":17,
        # "goals":2,
        # "team":"DAL",
        # "games":59,
        # "id":8480878
        return [Player(player_dict) for player_dict in self.response]

class PlayerStats():
    'presents the stats of the players'
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nationality):
        'sort'
        players = list(filter(lambda player: player.nationality == nationality, self.players))
        players.sort(key=lambda player: player.points, reverse=True)
        print(f'Players from {nationality}\n')
        return players


def main():
    'main function'
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    players = PlayerStats(reader.get_players())
    top_finnish_scorers = players.top_scorers_by_nationality("FIN")
    for player in top_finnish_scorers:
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
