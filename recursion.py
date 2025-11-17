def do_something(n: int):
    print(n)
    if n == 1:
        print("done with function")
        return
    do_something(n-1)

do_something(5)