from ai.minimax import Minimax
from ai.minimax_alpha_beta import MinimaxAlphaBeta
from ai.expected_minimax import Expectiminimax


class MinimaxFactory:
    def create(self, algorithm):
        if algorithm == 'Minimax':
            return Minimax()
        elif algorithm == 'Alpha-Beta Pruning Minimax':
            return MinimaxAlphaBeta()
        else:
            return Expectiminimax()
