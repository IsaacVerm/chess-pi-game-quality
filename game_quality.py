from get_games import LatestGame
from evaluate_games import EvaluateGame

stockfish_path = "/Users/isaacverminck/Downloads/stockfish-11-mac/Mac/stockfish-11-64"

# get game
latest_game = LatestGame()
latest_game.fetch()
raw_pgn = latest_game.pgn


# evaluate game
evaluate_game = EvaluateGame(stockfish_path)
evaluate_game.read(raw_pgn)
evaluate_game.score()
evaluate_game.determine_side()

print(evaluate_game.side)
