from music21 import chord


class Engine:
    def __init__(self):
        self.__is_active = True

    @property
    def is_active(self) -> bool:
        return self.__is_active

    def execute(self, value):
        if 'command' not in value:
            raise 'command is not specified'
        # コマンドごとに処理を分岐する
        command = value['command']
        if command == 'chord_name':
            return chord.Chord(value['notes']).pitchedCommonName
        elif command == 'exit':
            self.__is_active = False
        else:
            raise f'unexpected command: {command}'
        return {}
