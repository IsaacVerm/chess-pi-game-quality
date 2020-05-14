import requests

class LatestGame:
    url = 'https://lichess.org/api/user/isaacinator/current-game'
    headers = {'Accept': 'application/json'}
    game = None

    def fetch(self):
        self.game = requests.get(self.url, headers=self.headers).json()

    def moves(self):
        return self.game['moves']