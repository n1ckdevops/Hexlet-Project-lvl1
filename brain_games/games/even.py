from random import randint

GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_even(number: int) -> bool:

    if number % 2 == 0:
        return True
    return False


def game_settings() -> tuple:

    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    question: str = f"Question: {random_number}"
    if is_even(random_number):
        correct_answer: str = "yes"
    else:
        correct_answer: str = "no"
    return question, correct_answer
