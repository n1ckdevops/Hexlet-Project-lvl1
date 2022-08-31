import prompt
from random import randint


def is_brain_even():
    correct_answer = "yes"
    wrong_answer = "no"
    i = 0
    while i < 3:

        random_number = randint(1, 50)
        print('Answer "yes" if the number is even, otherwise answer "no"')
        question = f"Question: {random_number}"
        print(question)
        answer = prompt.string("Your answer: ")
        if answer == 'yes' and random_number % 2 == 0:
            print('Correct!')

        elif answer == 'no' and random_number % 2 != 0:
            print("Correct!")

        elif answer == 'yes' and random_number % 2 != 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {wrong_answer}.\n"
                  f"Let's try again,\n"
                  f"                ")

        elif answer == 'no' and random_number % 2 == 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again,\n"
                  f"                ")

        elif answer and random_number % 2 == 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {correct_answer}.\n"
                  f"Let's try again,\n"
                  f"                ")

        elif answer and random_number % 2 != 0:
            print(f"'{answer}' is wrong answer ;(. Correct answer was {wrong_answer}.\n"
                  f"Let's try again,\n"
                  f"                ")

    print("Congratulations, Bill!")


is_brain_even()
