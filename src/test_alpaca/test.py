#!/usr/bin/env python3

"""
test.py
"""

import sys
sys.path.append('../')

import unittest
from test_table import TestStateTransitionTable
from test_lex import TestLexParser
from test_lex import TestTokenStrategy
from test_syntax import TestSyntaxParser
from test_syntax import TestSyntaxParserError
from test_graph import TestGraph
from test_rast import TestRAST
from test_charset import TestCharacterSet
from test_nfa import TestNFA
from test_regex import TestRegex
from test_setrelation import TestSetRelation
from test_dfa import TestDFA
from test_dot import TestDot
from test_options import TestOptions
from test_input import TestInput
from test_output import TestOutput

if __name__ == '__main__':
    unittest.main(verbosity=2)

