import chess
import chess.engine
import chess.pgn
import io

class EvaluateGame:
    def __init__(self, stockfish_path):
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        self.game = None
        self.scores = []

    def read(self, raw_pgn):
        parsed_pgn = io.StringIO(raw_pgn)
        self.game = chess.pgn.read_game(parsed_pgn)

    def score(self):
        # set up the board in the starting position
        board = self.game.board()

        # go over each move and evaluate the position
        principal_line = self.game.mainline_moves()

        for move in principal_line:
            # make a move
            board.push(move)

            # analyse the new position
            analysis = self.engine.analyse(
                board=board, 
                limit=chess.engine.Limit(time=0.1))
            score = analysis['score'].white()

            # add score
            self.scores.append(score)
                
        # stop the process
        self.engine.quit()
