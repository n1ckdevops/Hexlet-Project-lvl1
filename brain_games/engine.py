import prompt
from brain_games.cli import welcome_user


def set_out(lets_play) -> None:
    # WELCOME LINES
    player_name: str = welcome_user()
    print(lets_play.GAME_MESSAGE)
    # SETTING OUT THE GAME
    attempts = 0
    while attempts != 3:
        question, correct_answer = lets_play.game_settings()
        print(question)
        player_answer = prompt.string("Answer: ")
        attempts += 1
        if player_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{player_answer} is wrong answer ;(. Correct "
                  f"answer is {correct_answer}")
            print(f"Let's try again, {player_name}!")
    print(f"Congratulations, {player_name}")
