from minimax_factory import MinimaxFactory
from service.Service import replace_at, COLUMNS, ROWS


class Agent:
    def __init__(self, algorithm_name, k, agent_turn="0"):
        self.k = k
        self.agent_turn = agent_turn
        self.current_state = 0
        self.algorithm = MinimaxFactory(agent_turn).create(algorithm_name)
        self.last_position = None

    def drop_disc(self, column):
        current_state_str = str(self.current_state).zfill(COLUMNS * ROWS)
        self.last_position = column
        for row in reversed(range(column, column + COLUMNS * ROWS, COLUMNS)):
            if current_state_str[row] == "0":
                current_state_str = replace_at(
                    current_state_str, row, str(1 + int(self.agent_turn))
                )
                break
        self.current_state = int(current_state_str)
        return self.current_state

    def play(self):
        state, _ = self.algorithm.decision(self.current_state, self.k)
        self.print_minimax_tree()
        return self.get_agent_decision(self.current_state, state)

    def get_agent_decision(self, current_state, max_state):
        current_state_str = str(current_state).zfill(COLUMNS * ROWS)
        max_state_str = str(max_state).zfill(COLUMNS * ROWS)
        idx = -1
        for i in range(COLUMNS * ROWS):
            if current_state_str[i] != max_state_str[i]:
                idx = i
                break
        col = idx % COLUMNS
        return col

    def print_minimax_tree(self):
        self.algorithm.get_minimax_tree()
