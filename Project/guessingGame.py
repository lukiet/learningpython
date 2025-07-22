from random import randint

guess = int(input('Enter a number between 1 - 10 : '))

num = randint(1, 10)

while guess !=num:
    if guess == num:
        print('Congrats you won !')
    elif guess > num:
        print('Try a smaller number ')
    elif guess < num:
        print('Try a bigger number ')
