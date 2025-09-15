import random

from typing import Self


class Anki:

    def __init__(self):
        self._words = {}

    def sanitize_input(self, string: str) -> str:
        return string.strip().lower()

    def add_word(self, word: str, translation: str) -> Self:
        """Добавляет слово в игру

        Parameters
        ---------
        word : str
            Слово для перевода
        translation : str
            Перевод слова

        Returns
        -------
        Anki

        Examples
        -------
        >>> anki.add_word('nino', 'мальчик')
        """
        self._words[self.sanitize_input(word)] = self.sanitize_input(translation)
        return self

    def get_card(self) -> str:
        word, _ = random.choice(list(self._words.items()))
        return word
    
    def check_translation(self, word: str, user_translation: str) -> bool:
        translation = self._words.get(self.sanitize_input(word))
        if translation is not None:
            return translation == self.sanitize_input(user_translation)
        return False

    def get_translation(self, word: str) -> str:
        return self._words.get(self.sanitize_input(word), '<UNKNOWN WORD>')
    
    def get_all_words(self):
        return self._words.items()
