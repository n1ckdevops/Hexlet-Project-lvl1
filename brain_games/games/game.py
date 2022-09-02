import prompt
from random import randint


def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")


def is_even():

    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i != 3:
        random_number = randint(1, 50)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        nothing = "yes" if answer == "no" else "no"
        if answer == 'yes' and random_number % 2 == 0:
            print('Correct!')
            i += 1
        elif answer == 'no' and random_number % 2 != 0:
            print("Correct!")
            i += 1
        elif answer == 'yes' and random_number % 2 != 0:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was {nothing}.\nLet's try again,\n")
            i *= 0
            return
        elif answer and random_number % 2 == 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was yes.\n"
                  f"Let's try again,\n"
                  f"                ")
            i *= 0
            return
        elif answer and random_number % 2 != 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was no.\n"
                  f"Let's try again,\n"
                  f"                ")
            return
    print("Congratulations, !")


is_even()
