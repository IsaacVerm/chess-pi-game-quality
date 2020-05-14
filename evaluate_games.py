import chess
import chess.engine
import chess.pgn
import io

class EvaluateGame:
    def __init__(self, stockfish_path):
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        self.game = None

    def read(self, raw_pgn):
        parsed_pgn = io.StringIO(raw_pgn)
        self.game = chess.pgn.read_game(parsed_pgn)

    def evaluate(self):
        # set up the board in the starting position
        board = self.game.board()

        # go over each move and evaluate the position
        principal_line = self.game.mainline_moves()

        for move in principal_line:
            while not board.is_game_over():
                result = self.engine.play(board, chess.engine.Limit(time=0.1))
                print(result)
                board.push(result.move)
        
        # stop the process
        self.engine.quit()
