from typing import List
from hangman_image import draw_hangman
from words import get_random_word


class Hangman:
    def __init__(self) -> None:
        self.word = get_random_word()
        self.correct_letters = set()
        self.incorrect_letters = set()
        self.incorrect_guesses = 0
        self.max_mistakes = 6
        self.max_attempts = 10

    def show_word(self) -> str:
        shown_word: List[str] = []
        for letter in self.word:
            if letter in self.correct_letters:
                shown_word.append(letter)
            else:
                shown_word.append("_")
        return "".join(shown_word)

    def play_game(self) -> None:
        print("Welcome to the Hangman Game!")
        print(self.show_word())

        while (
            self.incorrect_guesses < self.max_mistakes
            and len(self.correct_letters) < self.max_attempts
        ):
            guess = input("Guess a letter or a word: ").lower()

            if guess in self.correct_letters or guess in self.incorrect_letters:
                print("You already guessed that letter!")
                continue

            if len(guess) == 1:

                if guess in self.word:
                    self.correct_letters.add(guess)
                    print("Your guess is successful!")
                else:
                    self.incorrect_guesses += 1
                    self.incorrect_letters.add(guess)
                    print("Incorrect guess!")
            else:
                if guess == self.word:
                    print("Congrats! You guessed correctly!")
                    return
                else:
                    self.incorrect_guesses += 1
                    print("Incorrect guess!")

            print(self.show_word())
            draw_hangman(self.incorrect_guesses)

            if "_" not in self.show_word():
                print("Congrats! You guessed correctly!")
                return

            print("Attempts left:", self.max_mistakes - self.incorrect_guesses)

        print("Game over! Word was:", self.word)


if __name__ == "__main__":
    game = Hangman()
    game.play_game()
