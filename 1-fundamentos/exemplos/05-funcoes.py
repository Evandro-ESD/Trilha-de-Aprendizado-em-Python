# Exemplo: Funções

# Obs.:Um pouco da função print()
# Usando virgula ( , ) por padrão o print()
# separa os argumnentos com espaço


# Obs2:
# “Um parâmetro é uma variável da função que recebe um argumento quando a função é chamada.”
# O parâmetro ->  é o espaço reservado na definição da função.
# O argumento ->  é o valor real passado para esse espaço.


def exibe_hello_world():  # Sem parâmetro
    print("Hello World!")


exibe_hello_world()


def exibe_nome(name="World"):  # Com parâmetro defaut definido na criação da função
    print("Hello", name + "!")


exibe_nome()
exibe_nome("Python")  # Atribuindo argumentos


def two_params(params1, params2) -> int:  # Com dois parâmetros
    print(f"{params1}, {params2}!")


two_params("Hello", "Python")  # Dois argumentos


def arbitrary_arguments(
    *names,
):  # Permite vários parâmetros (dessa forma a função recebe uma tupla de argumentos)
    print(f"O nome: {names[2]}")  # Exibe que esta no índice ? names[?]


arbitrary_arguments("JavaScript", "Java", "Python")


def arbitrary_keyword_arguments(**linguagem):
    print(
        "**parâmetro → recebe vários argumentos nomeados (keyword arguments) e os armazena em um dicionário"
    )
    print(
        f"Exibir parâmetros nomeados -> tipo: {linguagem['tipo']} -> nome: {linguagem['name']}"
    )


arbitrary_keyword_arguments(name="Python", tipo="Liguagem de Programação")


def keyword_arguments(ling1, ling2, ling3):
    print(f"Linguagem de programação: {ling2}")
    print(f"Exibir todos os parârametros: {ling1} | {ling2} | {ling3}")


keyword_arguments(
    "Python", "Java", "JavaScript"
)  # Essa Função exige três argumentos mas só exibe o parâmetro especificado Ex: {ling1}
