import prompt
from random import randint


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def win_phrase(ans, name):
    if ans == 'Correct!':
        return print(f"Congratulations, {name}!")
    else:
        pass


def is_even() -> object:
    name = welcome_user()
    ans = 'Correct!'
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i != 3:
        random_number = randint(1, 50)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        nothing = "yes" if answer == "no" else "no"
        if answer == 'yes' and random_number % 2 == 0:
            print(ans)
            i += 1
        elif answer == 'no' and random_number % 2 != 0:
            print(ans)
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was {nothing}.\nLet's try again, {name}.")
            return
    win_phrase(ans, name)


is_even()