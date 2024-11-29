COLUMNS = 7
ROWS = 6
disk = ['1', '2']

def replace_at(state: str, ind: int, new_char: str):
    return (state[:ind] + new_char + state[ind + 1:])

def get_children(state: int, turn: str):
    '''
    Params:
        state (int): The current board state represented as an integer.
        turn (str): The current player's turn ('0' or '1').
        
    Returns:
        List[str]: A list of child states as strings.
    '''
    state_str = str(state)
    size = COLUMNS * ROWS

    state_str = state_str.zfill(size)

    print(state_str)
    columns = [0] * COLUMNS
    for i in range(ROWS):
        for j in range(COLUMNS):
            if state_str[i * COLUMNS + j] != '0':
                columns[j] = max(columns[j], ROWS - i)

    children = []
    for i in range(COLUMNS):
        if columns[i] < ROWS:
            index = (ROWS - columns[i] - 1) * COLUMNS + i
            new_state = replace_at(state_str, index, disk[int(turn)])
            children.append(new_state)

    return children