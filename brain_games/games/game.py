import random
from random import randint
import prompt


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


def correct_answer(random_1, random_2, exp):
    if exp == "-":
        equal = random_1 - random_2
        return equal
    elif exp == "+":
        equal = random_1 + random_2
        return equal
    else:
        equal = random_1 * random_2
        return equal


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no"')
    i = 0
    while i != 3:
        random_number = randint(1, 50)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")
        nothing = "yes" if answer == "no" else "no"
        if answer == 'yes' and random_number % 2 == 0:
            ans = 'Correct!'
            print(ans)
            i += 1
        elif answer == 'no' and random_number % 2 != 0:
            ans = 'Correct!'
            print(ans)
            i += 1
        else:
            ans = f"'{answer}' is wrong answer ;(.\
Correct answer was {nothing}.\nLet's try again, {name}.'"
            print(ans)
            i = 3

    win_phrase(ans, name)


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    while i != 3:
        random_1 = randint(31, 50)
        random_2 = randint(1, 10)
        exp = random.choice(["+", "-", "*"])
        correct_reply = correct_answer(random_1, random_2, exp)
        print(f"Question: {random_1} {exp} {random_2}")
        answer = prompt.string("Your answer: ")
        if exp == "-" and answer == str(random_1 - random_2):
            ans = 'Correct!'
            print(ans)
            i += 1
        elif exp == "+" and answer == str(random_1 + random_2):
            ans = 'Correct!'
            print(ans)
            i += 1
        elif exp == "*" and answer == str(random_1 * random_2):
            ans = 'Correct!'
            print(ans)
            i += 1
        else:
            ans = f"'{answer}' is wrong answer ;(.\
Correct answer was {correct_reply}.\nLet's try again, {name}.'"
            print(ans)
            i = 3
    win_phrase(ans, name)
