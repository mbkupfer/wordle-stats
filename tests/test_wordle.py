import pytest

from wordle import Wordle


@pytest.fixture
def world_game():
    return Wordle(word="globe")


def test_wordle_word(world_game):
    assert world_game.word == "globe"


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


def test_wordle_board_printout(world_game):
    world_game.guess("globe")
    board = world_game.print_board()
    assert (
        board
        == """1 G L O B E
2 _ _ _ _ _
3 _ _ _ _ _
4 _ _ _ _ _
5 _ _ _ _ _
"""
    )
