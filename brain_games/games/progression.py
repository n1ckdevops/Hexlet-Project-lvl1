from random import randint, randrange

GAME_MESSAGE = "What number is missing in this progression?"
MIN_INCR = 1
MAX_INCR = 5
ITERATIONS = 10
MIN_START = 1
MAX_START = 100


def game_settings():
    # starting number
    start_number = randint(MIN_START, MAX_START)
    # increments starting number of progression (so on so forth)
    incr_number = randint(MIN_INCR, MAX_INCR)
    # indexed number
    random_index_of_hidden_number = randrange(ITERATIONS)
    # var that stores th progression
    progression = f"{start_number} "
    # hidden number
    hidden_number = 0
    for i in range(ITERATIONS):
        # if random index of hidden number == 10...
        if random_index_of_hidden_number == i:
            # increases iteration
            start_number += incr_number
            # hidden number takes the place of start number
            hidden_number += start_number
            # and start number is {progression} which means
            # we change indexed number into ".. "
            progression += ".. "
        # if not...
        else:
            # increases iteration
            start_number += incr_number
            # and start number is {progression} which means
            # we give back the SAME number
            progression += f"{start_number}"
    # ask user the question
    question = f"Question: {progression}"
    # return to make it all work
    return question, str(hidden_number)
