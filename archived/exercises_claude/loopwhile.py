numeros_digitados = []  # lista pra guardar os números

while True:  # loop infinito
    numero = int(input("Digite um número (0 para sair): "))

    if numero == 0:  # se digitou 0, para o loop
        break

    numeros_digitados.append(numero)  # adiciona na lista
    print(f"Número {numero} adicionado!")

print(f"Você digitou os números: {numeros_digitados}")
print("Tchau!")

print("\n" + "=" * 40 + "\n")

# o claude que fez para mim e explicou o código