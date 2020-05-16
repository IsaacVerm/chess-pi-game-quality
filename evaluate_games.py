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
        self.score_diffs = None
        self.score_diffs_side_played = None

    def read(self, raw_pgn):
        parsed_pgn = io.StringIO(raw_pgn)
        self.game = chess.pgn.read_game(parsed_pgn)

    def get_score(self):
        def setup_board():
            return self.game.board()

        def get_principal_line():
            return self.game.mainline_moves()

        def analyse_position():
            analysis = self.engine.analyse(
                board=board,
                limit=chess.engine.Limit(time=0.1))

            return analysis

        def parse_score(analysis):
            score = analysis['score'].white().score(mate_score=100000)

            return score

        def append_score(score):
            self.scores.append(score)

        board = setup_board()

        for move in get_principal_line():
            board.push(move)
            analysis = analyse_position()
            score = parse_score(analysis)
            append_score(score)
        

    def stop_engine(self):
        self.engine.quit()

    def determine_side(self):
        headers = self.game.headers

        if headers['White'] == 'Isaacinator':
            self.side = 'white'
        else:
            self.side = 'black'

    def get_score_diffs(self):
        self.score_diffs = list(map(operator.sub, self.scores[1:], self.scores[:-1]))

    def get_score_diffs_side_played(self):
        # if you played white even score diffs are moves made by white
        # if you played black you aim for the odd score diffs
        # https://stackoverflow.com/a/12433705
        # slicing syntax is start:stop:end
        # I didn't specify the end so it goes on till the end of the list
        if self.side == 'white':
            start = 1
        else:
            start = 0

        step = 2

        self.score_diffs_side_played = self.score_diffs[start::step]

    def count_blunders(self):
        return None

    def count_great_moves(self):
        return None
