COLUMNS = 7
ROWS = 6
SIZE = COLUMNS * ROWS
disk = ['1', '2']


def get_children(state: int, turn: str):
    """
    Params:
        state (int): The current board state represented as an integer.
        turn (str): The current player's turn ('0' or '1').
        
    Returns:
        List[Tuple[str, int]]: A list of child states as integers and chosen column.
    """
    state_str = str(state)
    state_str = state_str.zfill(SIZE)

    columns_count = count_disks_per_column(state_str)
    children = []
    for i in range(COLUMNS):
        if columns_count[i] < ROWS:
            index = (ROWS - columns_count[i] - 1) * COLUMNS + i
            new_state = replace_at(state_str, index, turn)
            children.append((int(new_state), i))

    return children


def get_children_probability(state: int, turn: str, chosen_column: int):
    """
    Params:
        state (int): The current board state represented as an integer.
        turn (str): The current player's turn ('0' or '1').
        chosen_column (int): The column the player places the disk in.

    Returns:
        List[Tuple[str, float]]: A list of child states with their probabilities.
    """
    state_str = str(state)
    state_str = state_str.zfill(SIZE)

    columns_count = count_disks_per_column(state_str)
    children = []

    # Handle the chosen column
    if columns_count[chosen_column] < ROWS:
        index = (ROWS - columns_count[chosen_column] - 1) * COLUMNS + chosen_column
        new_state = replace_at(state_str, index, turn)
        probability = 0.75 if chosen_column == 0 or chosen_column == COLUMNS - 1 else 0.6
        children.append((int(new_state), probability))

    # Handle the left column
    if chosen_column > 0 and columns_count[chosen_column] < ROWS:
        index = (ROWS - columns_count[chosen_column]) * COLUMNS + chosen_column - 1
        new_state = replace_at(state_str, index, turn)
        probability = 0.25 if chosen_column == COLUMNS - 1 else 0.2
        children.append((int(new_state), probability))

    # Handle the right column
    if chosen_column < COLUMNS - 1 and columns_count[chosen_column] < ROWS:
        index = (ROWS - columns_count[chosen_column] - 1) * COLUMNS + chosen_column + 1
        new_state = replace_at(state_str, index, turn)
        probability = 0.25 if chosen_column == 0 else 0.2
        children.append((int(new_state), probability))

    return children


def replace_at(state: str, ind: int, new_char: str):
    return state[:ind] + new_char + state[ind + 1:]


def count_disks_per_column(state: str):
    columns = [0] * COLUMNS
    for i in range(ROWS):
        for j in range(COLUMNS):
            if state[i * COLUMNS + j] != '0':
                columns[j] = max(columns[j], ROWS - i)
    return columns


def eval(state: int):
    state_str = str(state)
    state_str = state_str.zfill(SIZE)
    board = [list(state_str[i * COLUMNS:(i + 1) * COLUMNS]) for i in range(ROWS)]
    return heuristic(board)


def heuristic(board):
    w4 = 8
    w3 = 4
    w2 = 2
    agent_4s = count_diagonal_disks(board, 1, 4) + count_vertical_disks(board, 1, 4) + count_horizontal_disks(board, 1,
                                                                                                              4)
    agent_3s = count_diagonal_disks(board, 1, 3) + count_vertical_disks(board, 1, 3) + count_horizontal_disks(board, 1,
                                                                                                              3)
    agent_2s = count_diagonal_disks(board, 1, 2) + count_vertical_disks(board, 1, 2) + count_horizontal_disks(board, 1,
                                                                                                              2)
    player_4s = count_diagonal_disks(board, 0, 4) + count_vertical_disks(board, 0, 4) + count_horizontal_disks(board, 0,
                                                                                                               4)
    player_3s = count_diagonal_disks(board, 0, 3) + count_vertical_disks(board, 0, 3) + count_horizontal_disks(board, 0,
                                                                                                               3)
    player_2s = count_diagonal_disks(board, 0, 2) + count_vertical_disks(board, 0, 2) + count_horizontal_disks(board, 0,
                                                                                                               2)

    return w4 * (agent_4s - player_4s) + w3 * (agent_3s - player_3s) + w2 * (agent_2s - player_2s)


def count_diagonal_disks(board, turn, num_of_disks):
    count = 0
    # from top-left to bottom-right
    for i in range(ROWS):
        for j in range(COLUMNS):
            current_count = 0
            for k in range(num_of_disks):
                if i + k == ROWS or j + k == COLUMNS or board[i + k][j + k] != disk[turn]:
                    break
                current_count += 1
            if current_count == num_of_disks:
                count += 1

    # from top-right to bottom-left
    for i in range(ROWS):
        for j in range(COLUMNS):
            current_count = 0
            for k in range(num_of_disks):
                if i - k < 0 or j + k >= COLUMNS or board[i - k][j + k] != disk[turn]:
                    break
                current_count += 1
            if current_count == num_of_disks:
                count += 1

    return count


def count_vertical_disks(board, turn, num_of_disks):
    count = 0
    for j in range(COLUMNS):
        for i in range(ROWS):
            current_count = 0
            for k in range(num_of_disks):
                if i + k == ROWS or board[i + k][j] != disk[turn]:
                    break
                current_count += 1
            if current_count == num_of_disks:
                count += 1
    return count


def count_horizontal_disks(board, turn, num_of_disks):
    count = 0
    for i in range(ROWS):
        for j in range(COLUMNS):
            current_count = 0
            for k in range(num_of_disks):
                if j + k == COLUMNS or board[i][j + k] != disk[turn]:
                    break
                current_count += 1
            if current_count == num_of_disks:
                count += 1
    return count
