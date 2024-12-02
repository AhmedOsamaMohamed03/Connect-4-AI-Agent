import time

from ai.minimax_factory import MinimaxFactory
from service.Service import *


class Agent:
    def __init__(self, algorithm_name, k):
        self.k = k
        self.current_state = 0
        self.algorithm = MinimaxFactory().create(algorithm_name)
        self.last_position = None

    def drop_disc(self, column):
        current_state_str = str(self.current_state).zfill(COLUMNS * ROWS)
        self.last_position = column
        for row in reversed(range(column, column + SIZE, COLUMNS)):
            if current_state_str[row] == "0":
                current_state_str = replace_at(
                    current_state_str, row, "1"
                )
                break
        self.current_state = current_state_str
        return self.current_state, self.calculate_score(0)

    def play(self):
        state, _ = self.algorithm.decision(int(self.current_state), self.k)
        agent_decision = self.get_agent_decision(self.current_state, state)
        self.current_state = str(state).zfill(SIZE)
        # self.print_minimax_tree()
        return agent_decision, self.calculate_score(1), self.algorithm.get_parent()

    def get_agent_decision(self, current_state, max_state):
        current_state_str = str(current_state).zfill(SIZE)
        max_state_str = str(max_state).zfill(SIZE)
        idx = -1
        for i in range(SIZE):
            if current_state_str[i] != max_state_str[i]:
                idx = i
                break
        col = idx % COLUMNS
        return col

    def print_minimax_tree(self):
        tree = self.algorithm.get_minimax_tree()
        i = 1
        for level in tree:
            print(f"level {i} -> {level}")
            # print(len(level))
            i += 1
        return tree

    def calculate_score(self, turn):
        self.current_state = str(self.current_state).zfill(SIZE)
        board = [list(self.current_state[i * COLUMNS:(i + 1) * COLUMNS]) for i in range(ROWS)]
        return (count_diagonal_disks(board, turn, 4) +
                count_vertical_disks(board, turn, 4) +
                count_horizontal_disks(board, turn, 4))


# if __name__ == '__main__':
#     start = time.time()
#     agent = Agent("minimax alpha beta", 4)
#     print(agent.drop_disc(3))
#     print(agent.play())
#     print(agent.drop_disc(4))
#     print(agent.play())
#     print(agent.drop_disc(2))
#     print(agent.play())
#     print(f"runtime: {time.time() - start}")
