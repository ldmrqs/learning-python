import random

numero_secreto = random.randint(1, 10)
print("🎲 Pensei em um número de 1 a 10!")
tentativa = int(input("Qual é seu palpite? "))

if tentativa == numero_secreto:
    print("🎉 ACERTOU! Você é bom nisso!")
elif tentativa < numero_secreto:
    print(f"📈 Muito baixo! O número era {numero_secreto}")
else:  # tentativa > numero_secreto
    print(f"📉 Muito alto! O número era {numero_secreto}")

print("="*50)

# versão melhorada do claude