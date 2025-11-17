from http.server import nobody

people = ['John', 'Paul', 'George', 'Ringo']
for beatle in people:
    print("Hello " + beatle) # or print(f"Hello {beatle}")
    
# range of numbers
for i in range(5):
    print(i)

# print bob ten times
for i in range(10):
    print("Bob")

mylist = ['apple', 'banana', 'cherry']
mylist[0] = 'kiwi'
print(mylist[1])
