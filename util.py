from enum import Enum


class Colors:
    """ANSI escape sequences for printing colors in command line"""

    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"


class GuessValue(Enum):
    CORRECT = object()
    WRONG_LOCATION = object()
    INCORRECT = object()


def cprint_clue(letter: str, guess_value: str) -> str:
    if guess_value is GuessValue.CORRECT:
        color = Colors.GREEN
    elif guess_value is GuessValue.WRONG_LOCATION:
        color = Colors.YELLOW
    elif guess_value is GuessValue.INCORRECT:
        color = Colors.RESET
    else:
        raise ValueError(guess_value)
    return f"{color}{letter}{Colors.RESET}"
