"""
sample_list = []

for i in range(10):
    sample_list.append(i)

print(sample_list)
"""

# list comprehensions:
sample_list2 = [i * 2 for i in range(10) if i % 2 == 0] # jeito mais clean para short line of codes
print(sample_list2)

# exemplo 2
people: list[str] = ["Mario", "Luigi", "Peach"]
cap_people = [person.upper() for person in ["Mario", "Luigi", "Peach"]]
print(cap_people)


