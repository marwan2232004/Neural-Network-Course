import random


# TODO [1]: implement the guessing_game function
def guessing_game(max_value: int, *, attempts: int):  # hint: a return type is tuple[bool, list[int], int]:
    secret_number: int = random.randint(1, max_value)
    attempt: int = 0
    guesses: list[int] = []
    post_message: str = f"Guess a number between 1 and {max_value} 🔢"
    try:
        while attempt < attempts:
            guess: int = int(input(f"Attempt {attempt}/{attempts}: \n {post_message} \n Enter your guess: "))
            guesses.append(guess)
            if guess == secret_number:
                return True, guesses, secret_number
            elif guess < secret_number:
                post_message = "Try guessing a higher number ☝️"
            else:
                post_message = "Try guessing a lower number 👇"
            attempt += 1
    except ValueError:
        raise ValueError("Invalid input entered")

    return False, guesses, secret_number


# TODO [2]: implement the play_game function
def play_game() -> None:
    max_value: int = 20
    attempts: int = 5
    while True:
        status, guesses, chosen_int = guessing_game(max_value, attempts=attempts)
        if status:
            assert chosen_int in guesses, "Error: The chosen number should be in the guesses list."
            print(f"Congratulations! You guessed the number in {len(guesses)} attempts 🎯")
            break
        else:
            assert chosen_int not in guesses, "Error: The chosen number should not be in the guesses list."
            message: str = (f"Sorry! You could not guess the number in {attempts} attempts. 👻\n"
                            f"The number was {chosen_int} 🙈\n"
                            f"Do you want to play again? 🎮 (yes/no):")
            play_again = input(message).strip().lower()
            if play_again != "yes":
                break

    print("Game Over!")
