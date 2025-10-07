# Exemplo: Loops (for, while)

###########################################################
# Exemplo for

# Iterando sobre a string (palavra) "Python"
# for letter in "Python":
#     print(letter)

# Iterando sobre a lista de linguagens
languages = ["JavaScript", "Java", "Python", "C#", "Python"]

# Índices correspondentes: 0, 1, 2, 3, 4

# Mostrar todas as palavras presentes na lista
# for language in languages:
#     print(language)

# Verificar se a palavra "Python" está presente na lista
# print(40 * "-")
# print("Dentro do loop for:")
# for language in languages:
#     if language == "Python":
#         print("'Python' está presente na lista de linguagens")
#         break
# else:
#     print("'Python' NÃO está presente na lista de linguagens")
# print(40 * "-")

# Usando lower() ou upper() para padronizar a comparação
# print(40 * "-")
# print("Dentro do loop for com lower():")
# for language in languages:
#     if language.lower() == "python":
#         print("'Python' está presente na lista de linguagens")
#         break
# else:
#     print("'Python' NÃO está presente na lista de linguagens")
# print(40 * "-")

# Forma comparativa sem loop
# if "Python" in languages:
#     print("'Python' está presente na lista de linguagens")
# else:
#     print("'Python' NÃO está presente na lista de linguagens")

###########################################################
# Exemplo com range()
print(40 * "-")
print("Dentro do loop range:")
print(f"{languages}")

print(40 * "-")
# Percorrendo com índice
for idx in range(0, len(languages)):
    print(f"Índice {idx}: {languages[idx]}")

print(40 * "-")
# range(start, stop, step)
print("range do start até stop-1 pulando de step em step (start=0, stop=5, step=2)")
for idx in range(0, len(languages), 2):
    print(f"Índice {idx}: {languages[idx]}")

print(40 * "-")
# range simples
print("range do start até stop-1 (start=0, stop=2)")
for idx in range(0, 2):
    print(f"Índice {idx}: {languages[idx]}")

print(40 * "-")
# Dupla iteração (linguagem x notas)
notas = ["Dez"]
for language in languages:
    for nota in notas:
        print(language.ljust(12), "->", nota)

print(40 * "-")

###########################################################
# Exemplo while
print("Exemplo de Liguagens com while:")
# Iniciamos a variável i = 0. No loop while, a validação acontece assim:
# - primeiro i = 0 e len(languages) = 5
# - os índices válidos vão de 0 a 4
# - a cada iteração i += 1
# - o loop continua até i = 5, quando a condição deixa de ser verdadeira e o loop é interrompido
i = 0
while i < len(languages):
    print(languages[i])
    i += 1

print(40 * "-")

# Exemplo com números
print("Exemplo com números:")
j = 1
while j < 6:
    print(j)
    j += 1

print(40 * "-")

# Exemplo while + if
print("Exemplo while + if:")
k = 11
while k < 16:
    print("k =", k)
    if k == 14:
        print("Atingiu a condição if... k =", k)
        break
    k += 1
