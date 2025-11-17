def greet_people(*people: str):
    print(people)
    for name in people:
        print(f"Hello {name}")


greet_people("Claude", "Josh", "Tyler", "Toad")

# keyword arguments
def do_something(**kwargs):
    print(kwargs)
    print(kwargs["name"]) # normal dictionary
do_something(name="Claude", age=20) # dictionary

# slash (/) and asterisk (*)

