import random


# Step 1: Create a list containing the names of your 5 favorite fruits.
word_list = ["Apple", "Mango", "Banana", "Cherry", "Strawberry"]

# Step 2: Print out the newly created list to the standard output (screen).
print(word_list)

# Step 3: Create the random.choice method and pass the word_list variable into the choice method
word = random.choice(word_list)  # Steps 3 and 4

# Step 4: Print out word to the standard output
print(word)

# Step 5: User input for a single letter guess
#guess = input("Please guess a single letter!")

# Step 6: Check the guess is 1 character and alphabetical 

while True:
    guess = input("Please guess a single letter!: ")

    if len(guess) == 1 and guess.isalpha():
        print("Good Guess :)")
        break
    elif len(guess) != 1 or not guess.isalpha():
        print("Oops! That is not a valid input.")
        continue