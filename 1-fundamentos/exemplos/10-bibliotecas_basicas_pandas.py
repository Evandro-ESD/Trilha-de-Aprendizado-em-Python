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


import pandas as pd


my_data_set = {
    "Produto": ["Maçã", "Banana", "Laranja", "Maçã", "Banana", "Laranja"],
    "Quantidade": [10, 15, 12, 8, 10, 18],
    "Preço": [2.50, 1.80, 3.00, 2.60, 1.90, 3.10],
}

df_vendas = pd.DataFrame(my_data_set)
print(df_vendas)
print(df_vendas.count(0, True))
print(df_vendas.head(0))  # Lista com nomes das colunas
print(
    df_vendas.head()
)  # 5 primeiras linhas ( (method) def head(n: int = 5) -> DataFrame )
# print(df_vendas["Produto"])
# ____________________________
print("\nResumo estatístico:")
print(df_vendas.describe().round(2))

# ____________________________
df_vendas["Receita"] = df_vendas["Quantidade"] * df_vendas["Preço"]
# print(df_vendas["Receita"])
# print(df_vendas)
# print("Receita média por produto")
receita_media_produto = df_vendas.groupby("Produto")["Receita"].mean()
# print(receita_media_produto)
# ____________________________


# Filtrar produtos com receita média acima de 20
print("\nProdutos com receita média acima de 20:")
print(receita_media_produto[receita_media_produto > 25])
