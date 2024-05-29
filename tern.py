age = int(input('Enter your age: '))
if age >= 18:
    message = 'You are an adult'
else:
    message = 'You are not an adult'

# below is an easier way to write the above code

message = "Adult" if age >= 18 else "Not an adult"

print(message)
