# # Exemplo: Bibliotecas Básicas

# """
# ref: https://www.insightlab.ufc.br/10-funcoes-mais-usadas-para-manipular-dataframes-no-pandas/
# algumas funções pandas
#       => unique e nunique
#       => describe
#       => sort_values
#       => value_counts
#       => isnull
#       => fillna
#       => groupby
#       => map e seu uso para codificação categórica
#       => apply e lambda
#       => pivot
# """


# import pandas as pd


# my_data_set = {
#     "Produto": ["Maçã", "Banana", "Laranja", "Maçã", "Banana", "Laranja"],
#     "Quantidade": [10, 15, 12, 8, 10, 18],
#     "Preço": [2.50, 1.80, 3.00, 2.60, 1.90, 3.10],
# }

# df_vendas = pd.DataFrame(my_data_set)
# # print(df_vendas)
# # print(df_vendas.count(0, True))
# # print(df_vendas.head(0))  # Lista com nomes das colunas
# # print(
# #     df_vendas.head()
# # )  # 5 primeiras linhas ( (method) def head(n: int = 5) -> DataFrame )
# # # print(df_vendas["Produto"])
# # ____________________________
# # print("\nResumo estatístico:")
# # print(df_vendas.describe().round(2))

# # ____________________________
# df_vendas["Receita"] = df_vendas["Quantidade"] * df_vendas["Preço"]
# # print(df_vendas["Receita"])
# # print(df_vendas)
# # print("Receita média por produto")
# receita_media_produto = df_vendas.groupby("Produto")["Receita"].mean()
# # print(receita_media_produto)
# # ____________________________


# # Filtrar produtos com receita média acima de 20
# print("\nProdutos com receita média acima de 20:")
# print(receita_media_produto[receita_media_produto > 25])


# -----  numpy ----- #
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

# import matplotlib.pyplot as plt
