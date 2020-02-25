"""
This file contains functions for creating a data for counter function and reference values
"""

import numpy as np
import json


def board_generator(n: int, max_length: int, max_count: int) -> (dict, int):
    """
    Iterative naive function for generation a board with ships for sea battle

    :param n: size of board (n x n)
    :param max_length: maximum length of the ship on board
    :param max_count: maximum number of ships on the board
    :return: board with ships, count of ships on this board
    """
    assert n > 1, 'Invalid n, 2x2 is a min size of the board'
    assert 1 < max_length <= n, 'Invalid max_length, ships length can be 2 to n'
    assert max_count > 0, 'Invalid max_count, max count is a natural number'

    # 1. Create a board:
    n += 2  # increase n to add a pad to boarder
    board = np.zeros((n, n))  # create a board with pad (pad used for check a free space on the borders)

    count_ships = 0
    iter_ = 1
    while count_ships < max_count:
        if not iter_ % 5000:
            # a lot of iterations ... seems there is no space on the board for a new ship
            break

        # 2. Create a ship:
        ship_length = np.random.randint(2, max_length + 1)  # length for new ship
        ship = np.zeros((3, ship_length + 2))  # ship with pad

        orient = np.random.rand() > .5  # random orient for new ship (0 - horizontal, 1 - vertical)
        if orient:
            ship = ship.T

        h, w = ship.shape  # height and width of ship mask
        ship[::h - 1, ::w - 1] = 1  # set ones to the corners of ship pad, because ships can touch diagonally

        # 3. Select a random area on the board:
        i, j = np.random.randint(n - h + 1), np.random.randint(n - w + 1)
        rnd_area = board[i:i + h, j:j + w]  # random place for a new ship

        # 4. Add a ship if place is free:
        area_is_empty = (rnd_area == rnd_area * ship).all()
        if area_is_empty:
            ship *= 0  # remove 1-corners
            ship[1:-1, 1:-1] += 1  # add body of a ship
            board[i:i + h, j:j + w] += ship  # add a ship to board
            count_ships += 1
        iter_ += 1

    # 5. Transform binary matrix into string format {0:'-', 1:'#'}
    board = board[1:-1, 1:-1]  # remove pad from board
    board = board.astype(object)
    board[board == 1] = '#'
    board[board == 0] = '-'

    result = {"board": '\n'.join(''.join(k for k in row) for row in board)}
    return result, count_ships


def json_writer(path: str, file: dict):
    """
    Save dict into json
    """
    with open(path, "w") as f:
        json.dump(file, f)


def generate_test_data(count_instances: int, min_board_size=10, max_board_size=1000):
    """
    Simple function to generate a random test data in resources folder
    """
    reference_values = dict()
    for data_id in range(count_instances):
        if not (data_id+1) % 10:
            print("Generated %d boards" % (data_id+1))
        param = np.random.randint(min_board_size, max_board_size)
        board_, true_value = board_generator(n=param, max_length=param, max_count=param)
        json_writer(path="resources/data/%i.json" % data_id, file=board_)
        reference_values[str(data_id)] = true_value

    json_writer(path="resources/reference_values.json", file=reference_values)


if __name__ == '__main__':
    generate_test_data(count_instances=100)
