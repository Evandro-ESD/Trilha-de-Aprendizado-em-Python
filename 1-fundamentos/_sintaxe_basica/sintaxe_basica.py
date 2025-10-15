# Instalação do Python

# https://www.python.org/

# Referências:
#  -> https://www.youtube.com/watch?v=-VeVq64Fgw0&t=26710s
#  -> https://www.w3schools.com/python/default.asp


# ===========================================
# Sintaxe Básica em Python
# Autor: Evandro
# Descrição: Este arquivo apresenta os conceitos fundamentais
# da sintaxe da linguagem Python de forma simples e prática.
# ===========================================

# Comentários ( #  e  """ """ )
# Comentário de uma linha

"""
Comentário de múltiplas linhas
Muito útil para documentar blocos maiores
"""

# ===========================================
# Saída de dados e f-strings
# ===========================================
nome = "Evandro"
idade = 37
print(f"Olá, meu nome é {nome} e tenho {idade} anos.")  # f-string
print("Soma de 2 + 2 =", 2 + 2)  # Exemplo de print simples

# ===========================================
# Tipos de dados básicos
# ===========================================
inteiro = 10
flutuante = 3.14
texto = "Python"
booleano = True

print(type(inteiro), type(flutuante), type(texto), type(booleano))

# ===========================================
# Variáveis e atribuição
# ===========================================
x = 5
y = 2
resultado = x + y
print("Resultado da soma:", resultado)

# ===========================================
# Entrada de dados (descomentando abaixo)
# ===========================================
# nome_usuario = input("Digite seu nome: ")
# print("Olá", nome_usuario)

# ===========================================
# Estruturas condicionais
# ===========================================
if x > y:
    print("x é maior que y")
elif x == y:
    print("x e y são iguais")
else:
    print("y é maior que x")

# ===========================================
# Laços de repetição
# ===========================================
print("👉 Exemplo com for:")
for i in range(3):
    print("Repetição número", i)

print("👉 Exemplo com while:")
contador = 0
while contador < 3:
    print("While:", contador)
    contador += 1

# ===========================================
# Listas e iteração
# ===========================================
linguagens = ["python", "javascript", "java"]
for linguagem in linguagens:
    print("Fruta:", linguagem)

# Adicionando e removendo elementos
linguagens.append("typescript")
linguagens.remove("java")
print("Lista atualizada:", linguagens)

# ===========================================
# Dicionário (dict)
# ===========================================
pessoa = {"nome": "Evandro", "idade": 37}
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])

# ===========================================
# Operadores de comparação e lógicos
# ===========================================
a = 10
b = 20
print(a == b, a != b, a > b, a < b)  # Comparação
print(a > 5 and b > 5)  # Lógico AND
print(a < 5 or b > 5)  # Lógico OR
print(not a == b)  # Lógico NOT


# ===========================================
# Funções simples
# ===========================================
def saudacao(nome):
    """Função que retorna uma saudação personalizada."""
    return f"Olá, {nome}!"


print(saudacao("Pythonista"))


# Função com retorno de soma
def somar(n1, n2):
    return n1 + n2


print("Soma:", somar(5, 7))

# ===========================================
# Boas práticas básicas
# ===========================================
# - Use nomes de variáveis descritivos.
# - Siga a indentação de 4 espaços.
# - Use comentários claros e objetivos.
# - Escreva funções pequenas e bem definidas.
# - Utilize docstrings para documentar funções.

# ===========================================
# Observações finais
# ===========================================
# - Python diferencia letras maiúsculas e minúsculas.
# - Não é necessário declarar tipo de variável.
# - A indentação define blocos de código.
# - Arquivos Python terminam com a extensão .py
