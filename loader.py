import json
import pathlib
import typing

from anki import Anki


class BaseLoader(typing.Protocol):

    anki: Anki

    def __init__(self, anki: Anki):
        self.anki = anki

    def __enter__(self) -> Anki:
        ...

    def __exit__(self, *args):
        ...


class JsonLoader(BaseLoader):

    def __enter__(self) -> Anki:
        path = pathlib.Path('data/words.json')
        if path.exists():
            with path.open() as file_input:
                words = json.load(file_input)
                for word, translation in words.items():
                    self.anki.add_word(word, translation)

        return self.anki

    def __exit__(self, *args):
        path = pathlib.Path('data/words.json')
        with path.open('w') as file_output:
            words = dict(self.anki.get_all_words())
            json.dump(words, file_output, ensure_ascii=False)


class TextLoader(BaseLoader):

    def __enter__(self) -> Anki:
        path = pathlib.Path('data/words.txt')
        if path.exists():
            with path.open() as file_input:
                # nino;мальчик
                for line in file_input:
                    line = line.strip()
                    word, sep, translation = line.partition(';')
                    self.anki.add_word(word, translation)

        return self.anki

    def __exit__(self, *args):
        path = pathlib.Path('data/words.txt')
        with path.open('w') as file_output:
            for word, translation in self.anki.get_all_words():
                file_output.write(f'{word};{translation}\n')


