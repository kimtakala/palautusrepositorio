import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_search_right_name(self):
        self.stats.search("Semenko")
    
    def test_search_wrong_name(self):
        self.stats.search("asdasdasd")
    
    def test_team(self):
        self.stats.team("EDM")

    def test_top(self):
        self.stats.top(2)

    def test_top_points(self):
        self.stats.top(2, SortBy.POINTS)

    def test_top_goals(self):
        self.stats.top(2, SortBy.GOALS)

    def test_top_assists(self):
        self.stats.top(2, SortBy.ASSISTS)