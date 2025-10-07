# # Exemplo: Funções

# # Obs.:Um pouco da função print()
# # Usando virgula ( , ) por padrão o print()
# # separa os argumnentos com espaço


# # Obs2:
# # “Um parâmetro é uma variável da função que recebe um argumento quando a função é chamada.”
# # O parâmetro ->  é o espaço reservado na definição da função.
# # O argumento ->  é o valor real passado para esse espaço.

# # Obs3:
# os argumentos padrão em Python (sem / ou *) são, por padrão, posicionais ou nomeados ao mesmo tempo.

# 👉 Ou seja:
# Você pode passá-los por posição,
# ou por nome,
# e o Python vai aceitar das duas formas.

#################################################################################
# def exibe_hello_world():  # Sem parâmetro
#     print("Hello World!")


# exibe_hello_world()


# def exibe_nome(name="World"):  # Com parâmetro defaut definido na criação da função
#     print("Hello", name + "!")


# exibe_nome()
# exibe_nome("Python")  # Atribuindo argumentos


# def two_params(params1, params2) -> int:  # Com dois parâmetros
#     print(f"{params1}, {params2}!")


# two_params("Hello", "Python")  # Dois argumentos


# def arbitrary_arguments(
#     *names,
# ):  # Permite vários parâmetros (dessa forma a função recebe uma tupla de argumentos)
#     print(f"O nome: {names[2]}")  # Exibe que esta no índice ? names[?]


# arbitrary_arguments("JavaScript", "Java", "Python")


# def arbitrary_keyword_arguments(**linguagem):
#     print(
#         "**parâmetro → recebe vários argumentos nomeados (keyword arguments) e os armazena em um dicionário"
#     )
#     print(
#         f"Exibir parâmetros nomeados -> tipo: {linguagem['tipo']} -> nome: {linguagem['name']}"
#     )


# arbitrary_keyword_arguments(name="Python", tipo="Liguagem de Programação")


# def keyword_arguments(ling1, ling2, ling3):
#     print(f"Linguagem de programação: {ling2}")
#     print(f"Exibir todos os parârametros: {ling1} | {ling2} | {ling3}")


# keyword_arguments(
#     "Python", "Java", "JavaScript"
# )  # Essa Função exige três argumentos mas só exibe o parâmetro especificado Ex: {ling1}


# _____________________________________________________________________________
def my_list(languages):
    for language in languages:
        print(language)


languages = ["Python", "Java", "JavaScript"]
my_list(languages)
# _____________________________________________________________________________

print(50 * "_")
print("Retorno de valores")
print(50 * "_")
# Retorno de valores


# _____________________________________________________________________________
def soma_simples(x):
    return x + 10


print(soma_simples(5))
print(soma_simples(15))
print(soma_simples(25))
# _____________________________________________________________________________

# Argumentos posicionais

# Um argumento posicional é aquele que é passado na ordem em que os parâmetros foram definidos na função.
# Ou seja, a posição importa.


def show_infos(name: str, age: int, /, language: str) -> str:
    print(
        f"Meu nome é {name}, tenho {age} anos de idade e minha linguagem é {language}"
    )


try:
    show_infos(
        "John", 78, "Python"
    )  # usando argumentos posicionais obrigatórios atens da /
    # show_infos(
    #     age=78,
    #     name="John",
    #     language="Python",  # Erro argumentos são posicionais não podem ser nomeados
    # )
    # show_infos()  # Erro: Sem argumentos
except Exception as e:
    print(e)
# ______________________________________________________________________________________________


def show_infos2(name: str, age: int, /, *, language: str) -> str:
    print(
        f"Meu nome é {name}, tenho {age} anos de idade e minha linguagem é {language}"
    )


try:
    # show_infos2("John", 78, "Python")  # Erro: usando argumentos posicionais
    show_infos(
        "John",
        78,
        language="Python",  # Erro argumentos são posicionais não podem ser nomeados
    )
    # show_infos()  # Erro: Sem argumentos
except Exception as e:
    print(e)
# ______________________________________________________________________________________________
