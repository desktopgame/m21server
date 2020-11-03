
import sys
import os
from unittest import TestCase
from music21server.engine import Engine


class MyTest(TestCase):
    def test_exit(self):
        print('test_exit.')
        e: Engine = Engine()
        e.debug = True
        print(e.execute({'command': 'exit'}))

    def test_chord_name(self):
        print('test_chord_name.')
        e: Engine = Engine()
        e.debug = True
        print(e.execute({'command': 'chord_name', 'notes': ['A', 'B', 'E']}))
