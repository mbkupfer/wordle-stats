from dataclasses import dataclass, field
from itertools import zip_longest


@dataclass
class Wordle:
    """Represents a single wordle puzzle"""

    word: str
    round: int = 1
    total_rounds: int = 5
    guesses: list[str] = field(default_factory=list)
    solved: bool = None

    def print_board(self) -> str:
        """Pretty print the game board"""
        # todo: add colors
        board = ""
        for rnd, guess in zip_longest(range(1, self.total_rounds + 1), self.guesses):
            line = f"{rnd} "
            if guess:
                pretty = [f"{c} " for c in guess]
                line += "".join(pretty).strip()
            else:
                line += "_ _ _ _ _"
            board += line + "\n"
        return board

    def guess(self, guess: str, return_board: bool = False) -> None:
        """Progress the state of the wordle puzzle"""

        if self.solved is None and self.round <= self.total_rounds:
            self.guesses += [guess.upper()]
            if guess.upper() == self.word.upper():
                self.solved = True
            elif self.round == self.total_rounds:
                self.solved = False
            else:
                self.round += 1
        if return_board:
            print(self.print_board())
