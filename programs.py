import math
import random

words = ["python", "hangman", "developer"]
    
word = random.choice(words)

word_display = "_ " * len(word)
    
print(f'Guess the word: {word_display}')