import requests

class LatestGame:
    url = 'https://lichess.org/api/user/isaacinator/current-game'
    pgn = None

    def fetch(self):
        self.pgn = requests.get(self.url).text
