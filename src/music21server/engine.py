from music21 import chord
from music21.chord import tables as chordTables
import itertools
import typing


class Engine(object):
    def __init__(self):
        self.__is_active = True
        self.__debug = False
        self.__chord_names = None

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, is_debbug: bool):
        self.__debug = is_debbug

    def chord_names(self) -> list:
        if self.__chord_names is not None:
            return self.__chord_names
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F',
                 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.__chord_names = []
        for item in list(itertools.permutations(notes, 4)):
            self.__chord_names.append({
                'recipe': item,
                'name': chord.Chord(item).pitchedCommonName
            })
        return self.__chord_names

    def execute(self, value):
        if 'command' not in value:
            raise 'command is not specified'
        if self.debug:
            print(f'- {value}')
        # コマンドごとに処理を分岐する
        command = value['command']
        if command == 'chord_name':
            return chord.Chord(value['notes']).pitchedCommonName
        elif command == 'chord_names':
            return map(lambda x: x['name'], self.chord_names())
        elif command == 'chord_infos':
            return map(lambda x: f'{x["recipe"]} => {x["name"]}', self.chord_names())
        elif command == 'recipe_by_name':
            return map(lambda x: x['recipe'], filter(lambda x: x['name'] == value['name'], self.chord_names()))
        elif command == 'exit':
            self.__is_active = False
        else:
            raise f'unexpected command: {command}'
        return {}
