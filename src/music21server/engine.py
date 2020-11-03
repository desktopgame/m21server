from music21 import chord


class Engine(object):
    def __init__(self):
        self.__is_active = True
        self.__debug = False

    @property
    def is_active(self) -> bool:
        return self.__is_active

    @property
    def debug(self) -> bool:
        return self.__debug

    @debug.setter
    def debug(self, is_debbug: bool):
        self.__debug = is_debbug

    def execute(self, value):
        if 'command' not in value:
            raise 'command is not specified'
        if self.debug:
            print(f'- {value}')
        # コマンドごとに処理を分岐する
        command = value['command']
        if command == 'chord_name':
            return chord.Chord(value['notes']).pitchedCommonName
        elif command == 'exit':
            self.__is_active = False
        else:
            raise f'unexpected command: {command}'
        return {}
