twenty_one_pilots = ["twenty one pilots", "clancy", "breach"] # valores dentro da lista
self_titled, clancy, breach = twenty_one_pilots
print(self_titled) # self_titled tá liberado porque é uma variável


pets: list[str] = ["arthur chandler", "john joey", "janis", "luna", "aurora", "kitana", "thor"] # dá pra adicionar outras coisas além de strings
print(pets)
print(len(pets)) # len serve para contar quantos elementos tem na lista
print(pets[-1]) # [-1] serve para selecionar um item da lista, nesse caso é o thor
print(pets[0:5]) # [0:5] serve para selecionar apenas do arthur até a aurora
print("thor" in pets) # vai retornar true porque o thor realmente tá na lista
print("jefa" in pets) # vai retornar falso porque a jefa não tá na lista


# próxima seção mostra como substituir o valor da lista
pets[0] = "tuitui"
print(pets)

# proxima seção mostra como adicionar um novo item sem substituir
pets.insert(0, "apollo")
print(pets)

# próxima seção mostra como adicionar um item no final da lista
pets.append("miguel")
print(pets)

# combinar listas
pets2: list[str] = ["marley", "beethoven"]
new_list = pets + pets2 # alternativas: pets += pets2, pets.extend(pets2)
print(new_list)

# remover itens da lista
discos: list[str] = ["paramore", "linkin park", "the smiths", "joy division"]
discos.remove("linkin park") # alternativa people.pop(1)
print(discos)

"""
comando para limpar completamente a lista: pets.clear
comando para restaurar completamente a lista: pets.reverse
comando para ordernar a lista: pets.sort
"""