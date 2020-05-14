import chess
import chess.engine
import chess.pgn
import io
import operator

class EvaluateGame:
    def __init__(self, stockfish_path):
        self.engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
        self.game = None
        self.scores = []
        self.side = None

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
            score = analysis['score'].white().score(mate_score=100000)

            # add score
            self.scores.append(score)
                
        # stop the process
        self.engine.quit()

    def determine_side(self):
        headers = self.game.headers

        if headers['White'] == 'Isaacinator':
            self.side = 'white'
        else:
            self.side = 'black'

    def score_diffs(self):
        self.score_diffs = list(map(operator.sub, self.scores[1:], self.scores[:-1]))
        print(self.score_diffs)

    def count_blunders(self):
        return None

    def count_great_moves(self):
        return None
