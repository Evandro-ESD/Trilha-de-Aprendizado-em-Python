# # Exemplo: Bibliotecas Básicas

# """


# # -----  numpy ----- #
import numpy as np

# Criando um array com valores de 0 a 4
a = np.array([0, 1, 2, 3, 4])
print("Array a:", a)

# Criando outro array com valores de 5 a 9
b = np.array([5, 6, 7, 8, 9])
print("Array b:", b)

# Soma elemento a elemento
soma = a + b
print("Soma (a + b):", soma)

# Multiplicação elemento a elemento
multiplicacao = a * b
print("Multiplicação (a * b):", multiplicacao)

# Funções matemáticas rápidas
print("Soma de todos os elementos de a:", np.sum(a))
print("Média dos elementos de b:", np.mean(b))
print("Maior valor em b:", np.max(b))
print("Menor valor em b:", np.min(b))

# Operações vetoriais
c = np.arange(0, 10, 2)  # de 0 a 10, pulando de 2 em 2
print("Array c (arange):", c)

# Mudando o shape de um array
matriz = np.arange(1, 10).reshape(3, 3)
print("Matriz 3x3:")
print(matriz)

# Selecionando elementos
print("Primeira linha da matriz:", matriz[0])
print("Elemento linha 2 coluna 3:", matriz[1, 2])

# -----  numpy ----- #
