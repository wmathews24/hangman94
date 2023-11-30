word_list = ["Apple", "Mango", "Banana", "Cherry", "Strawberry"]

def check_guess(guess):
    guess = guess.lower()

    if guess in word_list:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Enter your single letter guess: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Oops! That is not a valid input. Please enter a single letter.")
    check_guess(guess)

ask_for_input()
