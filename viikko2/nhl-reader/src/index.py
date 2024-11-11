'importing the necessities'
import requests
from rich.console import Console
from rich.table import Table
from rich import print
from player import Player

class PlayerReader():
    'reading the players from json and transforming them into classes'
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        'getting players'
        return [Player(player_dict) for player_dict in self.response]

class PlayerStats():
    'presents the stats of the players'
    def __init__(self, players):
        self.players = players
        self.nationalities = \
            "[" + "/".join(sorted(set(player.nationality for player in players))) + "]"

    def top_scorers_by_nationality(self, nationality):
        'sort and display top scorers for given nationality'
        players = list(filter(lambda player: player.nationality == nationality, self.players))
        players.sort(key=lambda player: (-player.points, -player.goals, player.name))

        table = Table(show_header=True, header_style="bold")
        table.add_column("name")
        table.add_column("team")
        table.add_column("goals", justify="right")
        table.add_column("assists", justify="right")
        table.add_column("points", justify="right")

        for player in players:
            table.add_row(
                f"[cyan]{player.name}[/cyan]",
                f"[magenta]{player.team}[/magenta]",
                f"[green]{player.goals}[/green]",
                f"[green]{player.assists}[/green]",
                f"[green]{player.goals + player.assists}[/green]"
            )

        print(f"\nTop scorers of {nationality} season 2024-25")
        console = Console()
        console.print(table)

def get_season_data(seasons):
    """Handle season selection and data retrieval."""
    seasons_display = f"[{'/'.join(seasons)}]"

    while True:
        season = input(
            f'Select season, leave empty to exit {seasons_display}: '
        ).strip()

        if not season:
            return None

        try:
            url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
            reader = PlayerReader(url)
            return PlayerStats(reader.get_players())
        except TypeError:
            print("[red]Invalid season. Please try again.\n[/red]")

def handle_nationality_selection(players):
    """Handle nationality selection and display stats."""
    while True:
        nationality = input(
            f'\nSelect nationality, leave empty to exit\n{players.nationalities}: '
        ).strip()

        if not nationality:
            break

        try:
            players.top_scorers_by_nationality(nationality)
        except ValueError:
            print("[red]Invalid nationality. Please try again.[/red]")

def main():
    """Main function for NHL Statistics application."""
    seasons = [
        "2018-19", "2019-20", "2020-21",
        "2021-22", "2022-23", "2023-24",
        "2024-25"
    ]

    print("[italic magenta]NHL Statistics by nationality[/italic magenta]")

    players = get_season_data(seasons)
    if players:
        handle_nationality_selection(players)

if __name__ == "__main__":
    main()
