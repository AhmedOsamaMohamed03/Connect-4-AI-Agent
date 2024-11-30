from minimax import Minimax
from minimax_alpha_beta import MinimaxAlphaBeta
from expected_minimax import Expectiminimax


class MinimaxFactory:
    def create(self, algorithm):
        if algorithm == 'minimax':
            return Minimax()
        elif algorithm == 'minimax alpha beta':
            return MinimaxAlphaBeta()
        else:
            return Expectiminimax()
