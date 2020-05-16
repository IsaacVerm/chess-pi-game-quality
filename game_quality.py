from get_games import LatestGame
from evaluate_games import EvaluateGame

stockfish_path = "/usr/games/stockfish"

# get game
latest_game = LatestGame()
latest_game.fetch()
raw_pgn = latest_game.pgn


# evaluate game
evaluate_game = EvaluateGame(stockfish_path)
evaluate_game.read(raw_pgn)
evaluate_game.determine_side()
evaluate_game.get_score()
evaluate_game.get_score_diffs()
evaluate_game.get_score_diffs_side_played()

# count moves 
blunder_count = evaluate_game.count_moves('blunder')
great_move_count = evaluate_game.count_moves('great_move')

print('side')
print(evaluate_game.side)
print('scores')
print(evaluate_game.scores)
print('score_diffs')
print(evaluate_game.score_diffs)
print('score_diffs_side_played')
print(evaluate_game.score_diffs_side_played)
print('blunder_count')
print(blunder_count)
print('great_move_count')
print(great_move_count)

# stop engine
evaluate_game.stop_engine()
