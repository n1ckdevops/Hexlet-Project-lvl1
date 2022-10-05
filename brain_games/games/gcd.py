from math import gcd
from random import randint

GAME_MESSAGE = 'Find the greatest common divisor of given numbers'
MIN_NUMBER = 1
MAX_NUMBER = 10


def game_settings():
    first_random = randint(MIN_NUMBER, MAX_NUMBER)
    second_random = randint(MIN_NUMBER, MAX_NUMBER)
    divisor = gcd(first_random, second_random)
    question = f"Question: {first_random} {second_random}"
    return question, str(divisor)
