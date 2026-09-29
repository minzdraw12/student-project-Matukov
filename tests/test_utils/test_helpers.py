from src.utils.helpers import greet, calculate_sum


def test_greet():
    assert greet("Иван") == "Привет, Иван! Добро пожаловать в проект."


def test_calculate_sum():
    assert calculate_sum(2, 3) == 5