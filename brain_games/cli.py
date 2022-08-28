#! brain_games/scripts/brain_games.py
import prompt
def welcome_user():
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
welcome_user()