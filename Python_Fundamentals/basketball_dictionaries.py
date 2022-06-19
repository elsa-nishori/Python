players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

# Update the constructor to accept a dictionary with a single player's information instead of individual arguments for the attributes.
class Player:
    def __init__(self, players):
        self.name = players['name']
        self.age = players['age']
        self.position = players['position']
        self.team = players['team']

    @classmethod
    def get_team(cls, team_list):
        player_list = []
        for team in team_list:
            player_list.append(team)
        return player_list

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

# Create your Player instances here!
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

new_team = []

# Write your for loop here to populate the new_team variable with Player objects.
for player_dict in players:
    new_team.append(player_dict)

print(new_team)

team_list = [
    {
    "name": "Lebron James", 
    "age":37, 
    "position": "small forward", 
    "team": "Los Angeles Lakers"
    },
    {
    "name": "Michael Jordan", 
    "age":59, 
    "position": "small forward", 
    "team": "Chicago Bullws"
    }
]

print(Player.get_team(team_list))