import random
from random import randint, choice
import prompt
import math
from sympy import isprime


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
    print('Answer "yes" if the number is even, otherwise answer "no".')
    ans = "Correct!"
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
            ans = f"'{answer}' is wrong answer ;(.\
Correct answer was {nothing}.\nLet's try again, {name}."
            print(ans)
            i = 3
    win_phrase(ans, name)


def calc():
    name = welcome_user()
    print('What is the result of the expression?')
    i = 0
    ans = "Correct!"
    while i != 3:
        random_1 = randint(31, 50)
        random_2 = randint(1, 10)
        exp = random.choice(["+", "-", "*"])
        correct_reply = correct_answer(random_1, random_2, exp)
        print(f"Question: {random_1} {exp} {random_2}")
        answer = prompt.string("Your answer: ")
        if exp == "-" and answer == str(random_1 - random_2):
            print(ans)
            i += 1
        elif exp == "+" and answer == str(random_1 + random_2):
            print(ans)
            i += 1
        elif exp == "*" and answer == str(random_1 * random_2):
            print(ans)
            i += 1
        else:
            ans = f"'{answer}' is wrong answer ;(. \
Correct answer was {correct_reply}.\nLet's try again, {name}."
            print(ans)
            i = 3
    win_phrase(ans, name)


def gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    ans = "Correct!"
    i = 0
    while i != 3:
        random_1 = randint(10, 20)
        random_2 = randint(10, 20)
        correct_reply = math.gcd(random_1, random_2)
        print(f"Question: {random_1} {random_2}")
        answer = int(prompt.string("Your answer: "))
        if answer == correct_reply:
            print(ans)
            i += 1
        else:
            ans = f"'{answer}' is wrong answer ;(. \
Correct answer was {correct_reply}.\nLet's try again, {name}."
            print(ans)
            break

    win_phrase(ans, name)


def progression():
    name = welcome_user()
    print('What number is missing in the progression?')

    counter = 0
    max_win = 3
    ans = "Correct!"
    while counter < max_win:
        prg_list = []
        start = randint(1, 10)
        step = randint(2, 7)
        stop_num = randint(6, 10)
        stop = start + (step * stop_num)
        for i in range(start, stop, step):
            prg_list.append(i)
        correct_reply = choice(prg_list)
        correct_index = prg_list.index(correct_reply)
        prg_list[correct_index] = ".."
        final_cut_prg = " ".join(map(str, prg_list))
        q = f"Question: {final_cut_prg}"
        print(q)
        answer = input("Your answer: ")
        if str(answer) == str(correct_reply):
            ans = 'Correct!'
            print(ans)
            counter += 1
        else:
            ans = f"'{answer}' is wrong answer ;(. \
Correct answer was {correct_reply}.\nLet's try again, {name}."
            print(ans)
            counter = 3
    win_phrase(ans, name)


def is_prime():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    ans = "Correct!"
    counter = 0
    while counter != 3:
        random_num = random.randint(3, 30)
        prime = isprime(random_num)
        q = f"Question: {random_num}"
        print(q)
        answer = input("Your answer: ")
        curr_reply = "yes" if answer == "no" else "no"
        if (answer == "yes") and prime:
            print(ans)
            counter += 1
        elif (answer == "no") and not prime:
            print(ans)
            counter += 1
        else:
            ans = f"'{answer}' is wrong answer ;(. \
Correct answer was {curr_reply}.\nLet's try again, {name}."
            print(ans)
            counter = 3
    win_phrase(ans, name)
