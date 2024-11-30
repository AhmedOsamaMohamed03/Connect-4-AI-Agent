from minimax import Minimax
from minimax_alpha_beta import MinimaxAlphaBeta


class MinimaxFactory:
    def create(self, algorithm):
        if algorithm == 'minimax':
            return Minimax()
        elif algorithm == 'minimax alpha beta':
            return MinimaxAlphaBeta()
        else:
            # TODO -> reserved for the expecti-minimax
            return None
