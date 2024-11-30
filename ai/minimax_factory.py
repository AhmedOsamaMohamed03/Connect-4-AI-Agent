from Minimax import Minimax
from minimax_alpha_beta import MinimaxAlphaBeta


class MinimaxFactory:
    def __init__(self, turn):
        self.turn = turn

    def create(self, algorithm):
        if algorithm == 'minimax':
            return Minimax(self.turn)
        elif algorithm == 'minimax alpha beta':
            return MinimaxAlphaBeta(self.turn)
        else:
            # TODO -> reserved for the expecti-minimax
            return None
