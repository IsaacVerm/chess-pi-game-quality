import requests

url = 'https://lichess.org/api/user/isaacinator/current-game'
headers = {'Accept': 'application/json'}

game = requests.get(url, headers=headers)

print(game.json())
