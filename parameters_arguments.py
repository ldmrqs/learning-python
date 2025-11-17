def greet(name: str, greeting: str = "Hello", age: int = 0): # default parameter
    print(
        f"{greeting}, {name}, {age}"
    )
greet("Claude", "Ciao")
greet("Josh", age=20)
greet(name="Tyler", age=20)

