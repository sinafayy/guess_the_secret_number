secret = 5

guess = int(input("Guess the secret number 1-10: "))

if guess == secret:
    print("Congratulations! You guessed the number 5!")
else:
    print("Better luck next time!")