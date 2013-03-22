"""
test_table.py
"""

import unittest
from table import StateTransitionTable

class TestStateTransitionTable(unittest.TestCase):
    def setUp(self):
        self.table = StateTransitionTable()

    def test_next_state(self):
        # START -> IN-ESCAPE
        self.assertEqual(self.table.next_state('START', '\\'), 'IN-ESCAPE')
        # START -> FINISH
        self.assertEqual(self.table.next_state('START', '|'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '*'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '+'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '('), 'FINISH')
        self.assertEqual(self.table.next_state('START', ')'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '.'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '^'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '['), 'FINISH')
        self.assertEqual(self.table.next_state('START', ']'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '-'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '0'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '1'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '2'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '3'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '4'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '5'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '6'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '7'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '8'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '9'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'a'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'b'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'c'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'd'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'e'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'f'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'g'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'h'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'i'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'j'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'k'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'l'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'm'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'n'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'o'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'p'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'q'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'r'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 's'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 't'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'u'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'v'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'w'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'x'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'y'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'z'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'A'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'B'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'C'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'D'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'E'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'F'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'G'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'H'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'I'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'J'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'K'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'L'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'M'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'N'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'O'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'P'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'Q'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'R'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'S'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'T'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'U'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'V'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'W'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'X'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'Y'), 'FINISH')
        self.assertEqual(self.table.next_state('START', 'Z'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '!'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '"'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '#'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '$'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '%'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '&'), 'FINISH')
        self.assertEqual(self.table.next_state('START', "'"), 'FINISH')
        self.assertEqual(self.table.next_state('START', ','), 'FINISH')
        self.assertEqual(self.table.next_state('START', '/'), 'FINISH')
        self.assertEqual(self.table.next_state('START', ':'), 'FINISH')
        self.assertEqual(self.table.next_state('START', ';'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '<'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '='), 'FINISH')
        self.assertEqual(self.table.next_state('START', '>'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '?'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '@'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '_'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '{'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '}'), 'FINISH')
        self.assertEqual(self.table.next_state('START', '~'), 'FINISH')
        # IN-ESCAPE -> FINISH
        self.assertEqual(self.table.next_state('IN-ESCAPE', '|'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '*'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '+'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '('), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', ')'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '\\'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '.'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '^'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '['), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', ']'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', '-'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'a'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'b'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'c'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'f'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'n'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'r'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 't'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'v'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'd'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'D'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'w'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'W'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 's'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'S'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'l'), 'FINISH')
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'C'), 'FINISH')
        # IN-ESCAPE -> None
        self.assertEqual(self.table.next_state('IN-ESCAPE', '0'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '1'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '2'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '3'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '4'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '5'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '6'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '7'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '8'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '9'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'e'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'g'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'h'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'i'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'j'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'k'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'm'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'o'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'p'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'q'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'u'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'x'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'y'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'z'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'A'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'B'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'E'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'F'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'G'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'H'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'I'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'J'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'K'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'L'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'M'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'N'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'O'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'P'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'Q'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'R'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'T'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'U'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'V'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'X'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'Y'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', 'Z'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '!'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '"'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '#'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '$'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '%'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '&'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', "'"), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', ','), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '/'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', ':'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', ';'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '<'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '='), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '>'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '?'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '@'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '_'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '{'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '}'), None)
        self.assertEqual(self.table.next_state('IN-ESCAPE', '~'), None)
        # FINISH -> None
        self.assertEqual(self.table.next_state('FINISH', '|'), None)
        self.assertEqual(self.table.next_state('FINISH', '*'), None)
        self.assertEqual(self.table.next_state('FINISH', '+'), None)
        self.assertEqual(self.table.next_state('FINISH', '('), None)
        self.assertEqual(self.table.next_state('FINISH', ')'), None)
        self.assertEqual(self.table.next_state('FINISH', '\\'), None)
        self.assertEqual(self.table.next_state('FINISH', '.'), None)
        self.assertEqual(self.table.next_state('FINISH', '^'), None)
        self.assertEqual(self.table.next_state('FINISH', '['), None)
        self.assertEqual(self.table.next_state('FINISH', ']'), None)
        self.assertEqual(self.table.next_state('FINISH', '-'), None)
        self.assertEqual(self.table.next_state('FINISH', '0'), None)
        self.assertEqual(self.table.next_state('FINISH', '1'), None)
        self.assertEqual(self.table.next_state('FINISH', '2'), None)
        self.assertEqual(self.table.next_state('FINISH', '3'), None)
        self.assertEqual(self.table.next_state('FINISH', '4'), None)
        self.assertEqual(self.table.next_state('FINISH', '5'), None)
        self.assertEqual(self.table.next_state('FINISH', '6'), None)
        self.assertEqual(self.table.next_state('FINISH', '7'), None)
        self.assertEqual(self.table.next_state('FINISH', '8'), None)
        self.assertEqual(self.table.next_state('FINISH', '9'), None)
        self.assertEqual(self.table.next_state('FINISH', 'a'), None)
        self.assertEqual(self.table.next_state('FINISH', 'b'), None)
        self.assertEqual(self.table.next_state('FINISH', 'c'), None)
        self.assertEqual(self.table.next_state('FINISH', 'd'), None)
        self.assertEqual(self.table.next_state('FINISH', 'e'), None)
        self.assertEqual(self.table.next_state('FINISH', 'f'), None)
        self.assertEqual(self.table.next_state('FINISH', 'g'), None)
        self.assertEqual(self.table.next_state('FINISH', 'h'), None)
        self.assertEqual(self.table.next_state('FINISH', 'i'), None)
        self.assertEqual(self.table.next_state('FINISH', 'j'), None)
        self.assertEqual(self.table.next_state('FINISH', 'k'), None)
        self.assertEqual(self.table.next_state('FINISH', 'l'), None)
        self.assertEqual(self.table.next_state('FINISH', 'm'), None)
        self.assertEqual(self.table.next_state('FINISH', 'n'), None)
        self.assertEqual(self.table.next_state('FINISH', 'o'), None)
        self.assertEqual(self.table.next_state('FINISH', 'p'), None)
        self.assertEqual(self.table.next_state('FINISH', 'q'), None)
        self.assertEqual(self.table.next_state('FINISH', 'r'), None)
        self.assertEqual(self.table.next_state('FINISH', 's'), None)
        self.assertEqual(self.table.next_state('FINISH', 't'), None)
        self.assertEqual(self.table.next_state('FINISH', 'u'), None)
        self.assertEqual(self.table.next_state('FINISH', 'v'), None)
        self.assertEqual(self.table.next_state('FINISH', 'w'), None)
        self.assertEqual(self.table.next_state('FINISH', 'x'), None)
        self.assertEqual(self.table.next_state('FINISH', 'y'), None)
        self.assertEqual(self.table.next_state('FINISH', 'z'), None)
        self.assertEqual(self.table.next_state('FINISH', 'A'), None)
        self.assertEqual(self.table.next_state('FINISH', 'B'), None)
        self.assertEqual(self.table.next_state('FINISH', 'C'), None)
        self.assertEqual(self.table.next_state('FINISH', 'D'), None)
        self.assertEqual(self.table.next_state('FINISH', 'E'), None)
        self.assertEqual(self.table.next_state('FINISH', 'F'), None)
        self.assertEqual(self.table.next_state('FINISH', 'G'), None)
        self.assertEqual(self.table.next_state('FINISH', 'H'), None)
        self.assertEqual(self.table.next_state('FINISH', 'I'), None)
        self.assertEqual(self.table.next_state('FINISH', 'J'), None)
        self.assertEqual(self.table.next_state('FINISH', 'K'), None)
        self.assertEqual(self.table.next_state('FINISH', 'L'), None)
        self.assertEqual(self.table.next_state('FINISH', 'M'), None)
        self.assertEqual(self.table.next_state('FINISH', 'N'), None)
        self.assertEqual(self.table.next_state('FINISH', 'O'), None)
        self.assertEqual(self.table.next_state('FINISH', 'P'), None)
        self.assertEqual(self.table.next_state('FINISH', 'Q'), None)
        self.assertEqual(self.table.next_state('FINISH', 'R'), None)
        self.assertEqual(self.table.next_state('FINISH', 'S'), None)
        self.assertEqual(self.table.next_state('FINISH', 'T'), None)
        self.assertEqual(self.table.next_state('FINISH', 'U'), None)
        self.assertEqual(self.table.next_state('FINISH', 'V'), None)
        self.assertEqual(self.table.next_state('FINISH', 'W'), None)
        self.assertEqual(self.table.next_state('FINISH', 'X'), None)
        self.assertEqual(self.table.next_state('FINISH', 'Y'), None)
        self.assertEqual(self.table.next_state('FINISH', 'Z'), None)
        self.assertEqual(self.table.next_state('FINISH', '!'), None)
        self.assertEqual(self.table.next_state('FINISH', '"'), None)
        self.assertEqual(self.table.next_state('FINISH', '#'), None)
        self.assertEqual(self.table.next_state('FINISH', '$'), None)
        self.assertEqual(self.table.next_state('FINISH', '%'), None)
        self.assertEqual(self.table.next_state('FINISH', '&'), None)
        self.assertEqual(self.table.next_state('FINISH', "'"), None)
        self.assertEqual(self.table.next_state('FINISH', ','), None)
        self.assertEqual(self.table.next_state('FINISH', '/'), None)
        self.assertEqual(self.table.next_state('FINISH', ':'), None)
        self.assertEqual(self.table.next_state('FINISH', ';'), None)
        self.assertEqual(self.table.next_state('FINISH', '<'), None)
        self.assertEqual(self.table.next_state('FINISH', '='), None)
        self.assertEqual(self.table.next_state('FINISH', '>'), None)
        self.assertEqual(self.table.next_state('FINISH', '?'), None)
        self.assertEqual(self.table.next_state('FINISH', '@'), None)
        self.assertEqual(self.table.next_state('FINISH', '_'), None)
        self.assertEqual(self.table.next_state('FINISH', '{'), None)
        self.assertEqual(self.table.next_state('FINISH', '}'), None)
        self.assertEqual(self.table.next_state('FINISH', '~'), None)

