# functions make the code cleaner and easier to read to not repeat myself.
def greet(name: str):
    print(f"Hey, {name}")
greet("Claude")
greet("Josh")

def music(instrument: str):
    print(f"I love to play {instrument}")
music("Guitar")

def do_something():
    for i in range(5):
        print("doing something")
    print("done")
do_something()


