# exemplo onde o usuário faz merda
#a = input("A: ")
#b = input("B: ")
#print("Sum:", int(a) + int(b))

# exemplo com try except & função
def do_math():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input)
        print(number)
    except ValueError:
       print("Please enter a valid number.")
       do_math()
    except Exception as e:
       print("Something went wrong:", e)

do_math()