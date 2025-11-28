import random
words = [
    # Easy (short, common words)
    "cat", "dog", "sun", "cup", "tree", "book", "fish", "milk", "bird", "rain",
    "ball", "shoe", "frog", "moon", "star", "snow", "cake", "ship", "king", "queen",

    # Medium (5–7 letters, everyday words)
    "puzzle", "orange", "planet", "rocket", "guitar", "castle", "winter", "summer",
    "banana", "pirate", "dragon", "jungle", "basket", "pencil", "butter", "flower",
    "silver", "purple", "friend", "family", "soccer", "rabbit", "bridge", "school",

    # Hard (longer, trickier words)
    "elephant", "dinosaur", "umbrella", "computer", "notebook", "mountain", "volcano",
    "airplane", "treasure", "adventure", "rainbow", "sandwich", "language", "holiday",
    "vampire", "phoenix", "journey", "monster", "history", "fantasy", "science",
    "circus", "wizard", "castle", "island",

    # Very Hard (less common, 8+ letters)
    "kangaroo", "alligator", "microscope", "astronomy", "mysterious", "laboratory",
    "chocolate", "astronaut", "fireworks", "reptilian", "revolution", "chemistry",
    "architecture", "electricity", "lightning", "explosion", "civilization",
    "encyclopedia", "philosophy", "psychology", "generation", "transportation",
    "communication", "imagination", "inspiration"
    
]
hangman_stages = [
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  /
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |   |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |
       |
       |
       |
    ---------
    """,
]


print("\nWelcome to the Word Guessing Game!")
print("You have 5 attempts to guess the word. Good luck!")


word = random.choice(words)
guessedWord = ["_"] * len(word)
attempts = 5
count = 5

print(hangman_stages[5])


while attempts > 0: 
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() :
        print("Invalid input.")
        continue
    if len(guess)>1:
        if guess == word:
            print('\nCongratulations! You guessed the word: ' + word)
            break
        else:
            attempts -= 1
            count -= 1
            print('You suck! That is not the word. Attempts left: ' + str(attempts))
            if count>0:
                print(hangman_stages[count])
            elif attempts == 0:
                print(hangman_stages[0])
            else:
                print(hangman_stages[count])
            continue
    if guess in guessedWord:
        print("You already guessed that letter. Try again.")
        continue
    if guess in word: 
        for i in range(len(word)):
            if word[i]==guess:
                guessedWord[i] = guess
        
        print('Amazing! You found a letter.')
    else:
        attempts -= 1
        count -= 1
        print('You suck! That letter is not in the word. Attempts left: ' + str(attempts))

    if count>0:
        print(hangman_stages[count])
    elif attempts == 0:
        print(hangman_stages[0])
    else:
        print(hangman_stages[count])
       
    if "_" not in guessedWord:
        print('\nCongratulations! You guessed the word: ' + word)
        break 
    if attempts == 0 and "_" in guessedWord:
     print('\nGame Over! The word was: ' + word + '. Better luck next time!\n')

    