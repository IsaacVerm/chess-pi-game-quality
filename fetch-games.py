import requests

class LatestGame:
    url = 'https://lichess.org/api/user/isaacinator/current-game'
    headers = {'Accept': 'application/json'}

    def fetch(self):
        return requests.get(self.url, headers=self.headers).json()

    