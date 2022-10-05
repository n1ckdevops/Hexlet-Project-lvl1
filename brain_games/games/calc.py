from random import randint, choice

GAME_MESSAGE = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 10
OPERATORS = ["+", "-", "*"]


def game_settings() -> tuple:
    """
    - return question and correct answer
    """
    first_number = randint(MIN_NUMBER, MAX_NUMBER)
    second_number = randint(MIN_NUMBER, MAX_NUMBER)
    operator = choice(OPERATORS)
    question = f"Question: {first_number} {operator} {second_number}"
    correct_answer = 0
    if operator == "+":
        correct_answer = first_number + second_number
    if operator == "-":
        correct_answer = first_number - second_number
    if operator == "*":
        correct_answer = first_number * second_number
    return question, str(correct_answer)
