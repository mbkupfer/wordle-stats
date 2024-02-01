import pytest

from wordle import Wordle
from util import GuessValue


@pytest.fixture
def world_game():
    return Wordle(word="globe")


def test_wordle_word(world_game):
    assert world_game.word == "GLOBE"


def test_throws_error_on_invalid_word():
    with pytest.raises(ValueError):
        Wordle("Elephant")


def test_wordle_solved(world_game):
    world_game.guess("globe")
    assert world_game.solved


def test_wordle_solved_mixed_case(world_game):
    world_game.guess("Globe")
    assert world_game.solved


def test_wordle_stop_after_max_rounds(world_game):
    for i in range(0, 5):
        world_game.guess("abcde")
    world_game.guess("green")
    assert len(world_game.guesses) == 5
    assert world_game.round == 5


def test_wordle_stops_when_solved(world_game):
    world_game.guess("globe")
    world_game.guess("black")
    assert world_game.round == 1
    assert world_game.solved


def test_check_value(world_game):
    world_game.guess("great")
    assert world_game.guesses[0][1] == (
        GuessValue.CORRECT,
        GuessValue.INCORRECT,
        GuessValue.WRONG_LOCATION,
        GuessValue.INCORRECT,
        GuessValue.INCORRECT,
    )
