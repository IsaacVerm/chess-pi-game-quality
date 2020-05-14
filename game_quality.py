from get_games import LatestGame

latest_game = LatestGame()
latest_game.fetch()
print(latest_game.pgn)
