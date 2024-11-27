class TennisGame:
    def __init__(self, player1_name: str, player2_name: str):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1
        else:
            raise KeyError("Incorrect player name!")
    
    def tie_game(self) -> str:
        if self.player1_score == 0:
            score = "Love-All"
        elif self.player1_score == 1:
            score = "Fifteen-All"
        elif self.player1_score == 2:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score
        
    def mid_game(self):
        scores = ["Love", "Fifteen", "Thirty", "Fourty"]
        return scores[self.player1_score] + "-" + scores[self.player2_score]

    def late_game(self) -> str:
        player1_advantage = self.player1_score - self.player2_score
        if player1_advantage == 1:
            score = "Advantage player1"
        elif player1_advantage == -1:
            score = "Advantage player2"
        elif player1_advantage >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def get_score(self):
        # tie handler
        if self.player1_score == self.player2_score:
            score = self.tie_game()

        # late game handler
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.late_game()

        # mid game handler
        else:
            score = self.mid_game()

        return score
