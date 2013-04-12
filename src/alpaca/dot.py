"""
dot.py
Dot for dot script
"""
from alpaca.charset import CharacterSet

class Dot:
    def __init__(self):
        self.script = ''
        self.script = self.script + 'digraph G {\n'
        self.script = self.script + '    graph [rankdir = LR, label = "Generated by alpaca.py 1.0\\n(C) 2013 activesys.wb@gmail.com"];\n'
        self.script = self.script + '    node [shape = circle];\n'

    def start(self, vs, vfs):
        self.script = self.script + '    start [shape = plaintext, label = ""];\n'
        self.script = self.script + '    start -> S%d [label = "start"];\n' % vs
        for vf in vfs:
            self.script = self.script + '    S%d [shape = doublecircle];\n' % vf

    def end(self):
        self.script = self.script + '}'

    def new_edge(self, vb, ve, e):
        if e in ('"', '\\') or e in CharacterSet.abbreviation:
            self.script = self.script + '    S%d -> S%d [label = "\\%s"];\n' % (vb, ve, e)
        else:
            self.script = self.script + '    S%d -> S%d [label = "%s"];\n' % (vb, ve, e)

