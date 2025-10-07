# Exemplo: Loops (for, while)


# Exemplo for

# # Iterando sobre a string (palavra) "Python"
# for letter in "Python":
#     print(letter)


# # iternado sobre a lista[] languagens
languages = ["JavaScript", "Java", "Python", "C#", "Python"]
# # # índices
# # # indices = [   "0",        "1",       "2",   "4"]

# # # Mostrar todas as palavras presentes na lista
# # for language in languages:
# #     print(language)

# # # Mostrar se a palavra "Python" está presente na lista.
# # print(40 * "-")
# # print("Dentro do loop for: ")
# # for language in languages:
# #     if language == "Python":
# #         print("'Python' está presente na lista de linguagens")
# #         break
# # else:
# #     print("'Python' NÃO está presente na lista de linguagens")
# # print(40 * "-")

# # # -------------------------------------------------#
# # # usando lower() "minusculas" ou upper() "maíusculas" para transformar as string.
# # print(40 * "-")
# # print("Dentro do loop for com lower(): ")
# # for language in languages:
# #     if language.lower() == "python":
# #         #  if language.upper() == "python":
# #         print("'Python' está presente na lista de linguagens")
# #         break
# # else:
# #     print("'Python' NÃO está presente na lista de linguagens")
# # print(40 * "-")
# # # -------------------------------------------------#


# # -------------------------------------------------#
# #  Duvida comparativa com for
# # if "Python" in languages:
# #     print("'Python' está presente na lista de linguagens")
# # else:
# #     print("'Python' NÃO está presente na lista de linguagens")
# # # -------------------------------------------------#


# # Exemplo com range()
# # for language in range(0, len(languages)):
# print("Dentro do loop range: ")
# print(f"{languages}")

# print(40 * "-")  # Apenas separa a exibição
# # _______________________________________________________
# for idx in range(0, len(languages)):
#     print(f"Índex {idx}: {languages[idx]}")

# print(40 * "-")  # Apenas separa a exibição
# # _______________________________________________________
# print(f"range do start até o stop-1 pulando de step em step, (star=0, stop=2, step=2)")
# for idx in range(0, len(languages), 2):
#     print(f"Índex {idx}: {languages[idx]}")

# print(40 * "-")  # Apenas separa a exibição
# # _______________________________________________________
# print(f"range do start até o stop-1, (star=0, stop=2)")
# for idx in range(0, 2):
#     print(f"Índex {idx}: {languages[idx]}")

# print(40 * "-")  # Apenas separa a exibição
# # _______________________________________________________
# notas = ["Dez"]
# for language in languages:
#     for nota in notas:
#         print(language.ljust(12), "->", nota)

# print(40 * "-")  # Apenas separa a exibição


###########################################################

# Exemplo while
# # _______________________________________________________
# "Inciamos a variável i = 0. No loop while a validação acontece
# da seguinte forma primeira validação i=0 e len(languages)=5,
# tamanho da lista languages -1, índices 0,1,2,3,4". i += 1 soma 1
# a variável i agora i=1 e a iteração continua até que i seja igual
#  a 5, então a condição deixa de ser válida e o loop é interrompido.

print(40 * "-")  # Apenas separa a exibição
print("Exemplo de Languagens:")
i = 0
while i < len(languages):
    print(languages[i])
    i += 1

print(40 * "-")  # Apenas separa a exibição

print("Exemplo com números:")
# # _______________________________________________________
j = 1
while j < 6:
    print(j)
    j += 1

print(40 * "-")  # Apenas separa a exibição
# # _______________________________________________________
print("Exemplo while + if:")
k = 11
while k < 16:
    print("k = ", k)
    if k == 14:
        print("Atingiu a condição if... k = ", k)
        break
    k += 1
