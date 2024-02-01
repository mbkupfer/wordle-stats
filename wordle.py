from dataclasses import dataclass, field
from itertools import zip_longest

from util import GuessValue, cprint_clue

@dataclass
class Wordle:
    """Represents a single wordle puzzle"""

    word: str
    round: int = 1
    total_rounds: int = 5
    guesses: list[str] = field(default_factory=list)
    solved: bool = None

    def __post_init__(self):
        self.word = self.word.upper()
        if len(self.word) != 5:
            raise ValueError(f"{self.word} is not a valid word.")

    def __str__(self):
        return self.print_board()

    def print_board(self) -> str:
        """Pretty print the game board"""

        board = ""
        for rnd, guess in zip_longest(range(1, self.total_rounds + 1), self.guesses):
            line = f"{rnd} "
            if guess:
                pretty = [
                    f"{cprint_clue(c, guess_value)} "
                    for c, guess_value in zip(guess[0], guess[1])
                ]
                line += "".join(pretty).strip()
            else:
                line += "_ _ _ _ _"
            board += line + "\n"
        if self.solved:
            board += "WINNER!"
        elif self.solved is not None:
            board += "GAME OVER"
        return board

    def guess(self, guess: str, return_board: bool = True) -> None:
        """Progress the state of the wordle puzzle"""

        if len(guess := guess.upper()) != 5:
            raise ValueError(f"{guess} is not a valid guess.")

        if self.solved is None and self.round <= self.total_rounds:
            check = []
            for i, letter in enumerate(guess):
                if letter == self.word[i]:
                    check.append(GuessValue.CORRECT)
                elif letter in self.word:
                    check.append(GuessValue.WRONG_LOCATION)
                else:
                    check.append(GuessValue.INCORRECT)
            self.guesses += [(guess, tuple(check))]
            if guess == self.word:
                self.solved = True
            elif self.round == self.total_rounds:
                self.solved = False
            else:
                self.round += 1
        if return_board:
            print(self.print_board())
