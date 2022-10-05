from random import randint, randrange

<<<<<<< HEAD
GAME_MESSAGE: str = "What number is missing in this progression?"
NUM_OF_ITERATIONS: int = 10
MIN_START: int = 1
MAX_START: int = 100
MIN_INC: int = 1
MAX_INC: int = 5
=======
GAME_MESSAGE = "What number is missing in this progression?"
MIN_INCR = 1
MAX_INCR = 5
ITERATIONS = 10
MIN_START = 1
MAX_START = 100
>>>>>>> 050d9db5d7c6b0361a87a26214c5cfb5f8184630


def game_settings() -> tuple:
    # Starting number of the progression
    starting_number: int = randint(MIN_START, MAX_START)
    # Increments the starting number and etc...
    increment_number: int = randint(MIN_INC, MAX_INC)
    # Which indexed number will be hidden
    random_index_of_hidden_number: int = randrange(NUM_OF_ITERATIONS)
    # Parameter, that stores the progression
    progress: str = f'{starting_number} '
    # hidden number
    hidden_number: int = 0
    for i in range(NUM_OF_ITERATIONS):
        if random_index_of_hidden_number == i:
            starting_number += increment_number
            hidden_number = starting_number
            progress += '.. '
        else:
            starting_number += increment_number
            progress += f'{starting_number} '
    question: str = f'Question: {progress}'
    return question, str(hidden_number)
