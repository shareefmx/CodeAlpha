import random

def choose_word():
    words = ["instagram","facebook","whatsapp", "codealpha","intenship","python", "programming", "code", "developer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

max_attempts = 6
incorrect_attempts = 0
guessed_letters = []
word_to_guess = choose_word()
print("Welcome to Hangman!")
print(display_word(word_to_guess, guessed_letters))
while "_" in display_word(word_to_guess, guessed_letters) and incorrect_attempts < max_attempts:
    guess = input("Guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue
    guessed_letters.append(guess)
    if guess not in word_to_guess:
        incorrect_attempts += 1
        print(f"Incorrect guess! {max_attempts - incorrect_attempts} attempts remaining.")
    print(display_word(word_to_guess, guessed_letters))
if "_" not in display_word(word_to_guess, guessed_letters):
    print("Congratulations! You guessed the word.")
else:
    print(f"Sorry, you're out of attempts. The word was: {word_to_guess}")