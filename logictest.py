name = input("What is your name? ")

if not name.strip():
    print("Name is empty")



age = int(input("How old are you?"))

if 18 <= age < 45:
    print('You are not old')
