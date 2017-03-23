# *** Hangman ***
# Convert integers to binary and back
#
# Usage:
# Open a terminal and enter the following command while in the
# directory you downloaded Hangman to: python3 Hangman.py
#
# License: BSD

import random

class Game:
    def __init__(self):
        self.word_list = [
            'pie', 'browser', 'snake', 'language', 'department', 'classroom', 'virtualization',
            'country', 'friendship', 'united', 'government', 'king', 'emperor', 'queen', 'music'
        ]

        print ('*** HANGMAN ***')

    def start(self):
        print ('Starting new game... you have seven lives! Good luck!')

        self.word = random.choice(self.word_list)
        self.won = False
        self.lost = False

        self.current_letters = []
        self.used_letters = []
        self.correct_moves = 0
        self.wrong_moves = 0

        for i in range(0, len(self.word)):
            self.current_letters.append('_')

        while not self.won and not self.lost:
            self.lost = self.has_lost()

            for i in self.current_letters:
                print (i, end=' ')

            print ('Used letters:', end=' ')
            for i in self.used_letters:
                print (i, end=' ')

            self.request_input()

            self.won = '' . join(self.current_letters) == self.word

        print (self.word)

        if self.lost:
            print ('You lost... :(')
        else:
            print ('Yay, you won!')

    def make_move(self, letter):
        for key,value in enumerate(self.word):
            if value == letter:
                self.current_letters[key] = letter
                found = True
            else:
                found = False

        self.used_letters.append(letter)

        if found:
            self.correct_moves += 1
        else:
            self.wrong_moves += 1

    def request_input(self):
        print ('\n\nPlease enter a letter')
        letter = input()

        if len(letter) != 1:
            print ('Invalid input!')
            return
        elif letter in self.used_letters:
            print ('You have already used that letter before!')
            return

        self.make_move(letter.lower())

    def has_lost(self):
        return True if self.wrong_moves > 7 else False

if __name__ == '__main__':
    game = Game()

    while True:
        game.start()

        print ('Play another game? Enter [quit] to exit, or press enter to proceed.')
        command = input()

        if command == 'quit':
            break
