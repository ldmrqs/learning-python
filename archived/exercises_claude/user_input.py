# peça a idade e diga se a pessoa pode dirigir (18+)

print("Greetings, stranger. What's your name?")
name = input('Enter your name: ')
print("Nice to meet you, " + name)
print("How old are you?")
age = input('Enter your age: ')
age = int(age)
if age >= 18:
    print("Alright, you can drive. Go head!")
else:
    print("Sorry, you can't drive.")
