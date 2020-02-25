"""
File for test
"""

import unittest
import glob
import json
from main import counter


def json_reader(path) -> dict:
    """
    Read json file
    """
    with open(path, "r") as f:
        json_ = json.load(f)
    return json_


class Test(unittest.TestCase):
    def test_counter(self):
        """
        Test counter function from main.py file
        """
        files = glob.glob('resources/data/*.json')
        values = dict()
        for file in files:
            board = json_reader(file)
            filename = int(file.split('/')[-1][:-5])
            values[str(filename)] = counter(board)['count_ships']

        reference_values = json_reader('resources/reference_values.json')
        self.assertDictEqual(values, reference_values, 'Invalid number of ships')


if __name__ == '__main__':
    unittest.main()
