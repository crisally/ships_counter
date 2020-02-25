"""
File contains main function, that calculates a ship's count on a board.
"""

from fastapi import FastAPI

app = FastAPI()


@app.post('/counter')
def counter(data: dict) -> dict:
    """
    Calculate a count of ships on the board.
    Ship is a sequence of "#" more than 2. ("#" is not a ship)

    :param data: sea battle board
    :return: count of ships
    """
    board = data.get('board').split()

    matrix = [list(row) for row in board]  # transform str board into matrix
    matrix += list(map(list, zip(*matrix)))  # add columns by matrix transpose to calculate a vertical ships

    flatten = '-'.join(''.join(row) for row in matrix)  # flatten matrix back into string format 1d
    ships = flatten.split('-')  # list with empty str, ship parts and ships ('', '#', '###')

    count = sum(1 for ship in ships if len(ship) > 1)  # count ships
    return {'count_ships': count}
