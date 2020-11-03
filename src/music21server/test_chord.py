
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

    def test_chord_names(self):
        print('test_chord_name.')
        e: Engine = Engine()
        e.debug = True
        for item in e.execute({'command': 'chord_names'}):
            print(item)

    def test_chord_infos(self):
        print('test_chord_infos.')
        e: Engine = Engine()
        e.debug = True
        for item in e.execute({'command': 'chord_infos'}):
            print(item)

    def test_recipe_by_name(self):
        print('test_recipe_by_name.')
        e: Engine = Engine()
        e.debug = True
        for item in e.execute({'command': 'recipe_by_name', 'name': 'G#-chromatic tetramirror'}):
            print(item)
