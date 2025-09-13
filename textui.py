import sys
import textwrap
from anki import Anki


class TextUI:

    def __init__(self, anki: Anki):
        self.anki = anki

    def start_game(self):
        print('Игра начинается. Для выхода введите: /exit')
        while True:
            word = self.anki.get_card()

            print(f'Ваше слово: {word}')

            user_translation = input('Введите перевод: ')
            
            if user_translation == '/exit':
                break

            if self.anki.check_translation(word, user_translation):
                print('Совершенно верно!')
            else:
                print(f'Неправильно :( Корректный перевод: {self.anki.get_translation(word)}')

    def add_words(self):
        print('Добавление новых слов. Для выхода введите: /exit')
        while True:
            word = input('Введите слово для перевода: ')
            if word == '/exit':
                break
            
            translation = input('Введите перевод слова: ')
            if translation == '/exit':
                break

            self.anki.add_word(word, translation)

    def main_loop(self):
        while True:
            print(
                textwrap.dedent(
                    """\
                    Меню (введите число):
                    1. Начало игры
                    2. Ввод новых слов
                    3. Выход"""
                )
            )
            user_choice = int(input())
            if user_choice == 1:
                self.start_game()
            elif user_choice == 2:
                self.add_words()
            elif user_choice == 3:
                sys.exit()
