class Player:
    '''
    A class for the NHL PLayers
    dicti format:
    {
        "name":"Nils Lundkvist",
        "nationality":"SWE",
        "assists":17,
        "goals":2,
        "team":"DAL",
        "games":59,
        "id":8480878
    }
    '''
    def __init__(self, dicti):
        self.name = dicti['name']
        self.nationality = dicti['nationality']
        self.assists = dicti['assists']
        self.goals = dicti['goals']
        self.points = self.assists + self.goals
        self.team = dicti['team']
        self.games = dicti['games']
        self.id = dicti['id']

    def __str__(self):
        return self.name
