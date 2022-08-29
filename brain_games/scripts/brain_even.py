import prompt
from random import randint


random_number = randint(1, 100)


correct_answer = "yes"
wrong_answer = "no"
#string = ''


def is_brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    question = f"Question: {random_number}"
    print(question)
    answer = prompt.string("Your answer: ")
    print(answer)
    if random_number % 2 == 0 and answer == correct_answer:
        print('Correct!')
    else:
        print(f"""'{answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again,
        """)


is_brain_even()
  #
