guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess the number: "))

if answer == guess:
    print("You guessed correctly")
