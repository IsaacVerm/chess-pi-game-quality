from get_games import LatestGame
from evaluate_games import EvaluateGame

stockfish_path = "/Users/isaacverminck/Downloads/stockfish-11-mac/Mac/stockfish-11-64"

# get game
latest_game = LatestGame()
latest_game.fetch()
raw_pgn = latest_game.pgn

# evaluate game
evaluation = EvaluateGame(stockfish_path)
evaluation.read(raw_pgn)
print(evaluation.game)
