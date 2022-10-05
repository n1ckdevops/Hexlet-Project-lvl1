from random import randint

GAME_MESSAGE = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100

# Function whether the number is prime or not


def is_prime(number):
    if number < 0:
        return False  # Negative numbers cant be prime
    for i in range(2, number):
        if number % 2 == 0:
            return False
    return True


def game_settings():
    """
    : return question and correct answer
    """
    random_number: int = randint(MIN_NUMBER, MAX_NUMBER)
    question: str = f"Question: {random_number}"
    if is_prime(random_number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
