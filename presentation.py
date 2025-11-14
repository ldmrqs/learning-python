# Dicionário com minhas informações
larissa = {
    "name": "Larissa D. Marques",
    "role": "Infrastructure Engineer & AI Engineer @ Thoughtworks",
    "email_address": {
        "TW": "larissa.dornelles@thoughtworks.com",
        "personal": "larissa@ldmrqs.com",
        "professional": "contact@ldmrqs.com"
    },
    "projects": "i've created POCs, demos with MCPs, and now I'm working with AI evals",
    "problems": "vibe-coding, when it comes to coding, I don't know what to do this is bothering me a lot.",
    "solution": "i decided to take the AI Engineer course on Campus, learning python from scratch and stop depending on AI to code.",
    "mindset": "AI is supposed to be my best friend, a companion, and not my brain."
}

# Versão inicial - imprime tudo numa linha só
print("=== Versão Simples ===")
print(larissa)
print("\n")

# Versão que só imprime valores
print("=== Só valores ===")
for value in larissa.values():
    print(value)
print("\n")

# Versão com chave e valor (mas email ainda aparece como dict)
print("=== Chave e Valor (básico) ===")
for key, value in larissa.items():
    print(key, value)
print("\n")

# VERSÃO FINAL - Formatada com tratamento especial para dicionários internos
print("=== Versão Formatada (Final) ===")
for key, value in larissa.items():
    if type(value) == dict:  # SE o valor for um dicionário
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:  # SE for um valor simples (string)
        print(f"{key}: {value}")

# Anotações do que aprendi:
"""
CONCEITOS APRENDIDOS:
1. .items() retorna pares (chave, valor)
2. .values() retorna apenas os valores
3. for key, value são variáveis GENÉRICAS - podem ter qualquer nome!
4. type(value) == dict verifica se é um dicionário
5. Posso fazer loops aninhados para dicionários dentro de dicionários
6. value.items() funciona porque 'value' É o dicionário interno naquele momento
7. Indentação do else IMPORTA - tem que estar alinhado com o if
8. Python não "sabe" o que os nomes significam - é a POSIÇÃO que importa

EVOLUÇÃO DO CÓDIGO:
- Tentei com my_name, role (achando que tinha que combinar com o conteúdo)
- Descobri que são variáveis genéricas que recebem CADA par
- Aprendi a tratar dicionários aninhados com if/else
- Entendi escopo de variáveis (só posso usar o que existe!)
"""
