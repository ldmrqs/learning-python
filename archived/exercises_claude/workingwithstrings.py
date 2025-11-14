def contar_vogais(string):
    string = string.lower()
    result = {}
    vogais = 'aeiou'
    for i in vogais:
        if i in string:
            result[i] = string.count(i)
    return result
print(contar_vogais("hello"))

# vi essa no stackoverflow