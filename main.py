import argparse
import typing
import pathlib

from anki import Anki
from textui import TextUI
from loader import BaseLoader, TextLoader, JsonLoader


def get_loader(file_ext: str) -> typing.Type[BaseLoader]:
    if file_ext == '.txt':
        return TextLoader
    elif file_ext == '.json':
        return JsonLoader
    raise ValueError("Unknown file type")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename')

    args = parser.parse_args()

    path = pathlib.Path(args.filename)
    
    loader = get_loader(path.suffix)

    anki = Anki()

    with loader(anki) as anki:
        ui = TextUI(anki)
        ui.main_loop()
