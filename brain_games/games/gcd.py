from math import gcd
from random import randint

GAME_MESSAGE = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 30


def game_settings():
    """
    :return: question and correct answer
    """
    first_random = randint(MIN_NUMBER, MAX_NUMBER)
    second_random = randint(MIN_NUMBER, MAX_NUMBER)
    divisor = gcd(first_random, second_random)
    question = f"Question: {first_random} {second_random}"
    return str(divisor), question
