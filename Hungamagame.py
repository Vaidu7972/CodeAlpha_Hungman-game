import random

# List of predefined words
word_list = ["apple", "banana", "cherry", "grape", "orange"]

# Randomly select a word from the list
selected_word = random.choice(word_list)
word_length = len(selected_word)

# Game setup
guessed_letters = []
correct_letters = ["_"] * word_length
max_attempts = 6
wrong_guesses = 0

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(" ".join(correct_letters))

# Main game loop
while wrong_guesses < max_attempts and "_" in correct_letters:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in selected_word:
        print("✅ Good guess!")
        for i in range(word_length):
            if selected_word[i] == guess:
                correct_letters[i] = guess
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! Attempts left: {max_attempts - wrong_guesses}")

    print("Word: " + " ".join(correct_letters))

# Game result
if "_" not in correct_letters:
    print("\n🎉 Congratulations! You guessed the word:", selected_word)
else:
    print("\n💀 Game Over! The word was:", selected_word)
