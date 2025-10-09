# Exemplo: Listas, Tuplas, Dicionários e Sets

# --------------------------------------------------------
# LISTA  [] → lista (ordenada, mutável, aceita duplicatas)
# --------------------------------------------------------
# Inserir: append(), insert()
# Remover: remove(), pop(), clear()
# Editar: lista[i] = valor
# Observações: mutável, ordenada, permite repetidos
lista = []

# --------------------------------------------------------
# CONJUNTO (SET):  () → conjunto (não ordenado, sem duplicatas)
# --------------------------------------------------------
# Inserir: add(), update()
# Remover: remove(), discard(), pop(), clear()
# Editar: não há (remover + adicionar)
# Observações: mutável, sem ordem, não permite duplicados
set = ()

# --------------------------------------------------------
# TUPLA: () → tupla (ordenada, imutável, aceita duplicatas)
# --------------------------------------------------------
# Inserir/Remover/Editar: imutável (converter para lista para alterar)
# Observações: ordenada, permite repetidos
tupla = ()
print()  # só para pular linha
# Criando uma tupla
tupla = ("Evandro", 37, True)
print("tupla:", tupla)

# Acessando elementos
print("primeiro elemento:", tupla[0])
print("último elemento:", tupla[-1])

# Tentando modificar (gera erro)
# tupla[1] = 38  # -> ERRO! Tuplas são imutáveis

# Para alterar, convertemos em lista
lista_temp = list(tupla)
lista_temp[1] = 38
tupla = tuple(lista_temp)
print("tupla modificada:", tupla)


# --------------------------------------------------------
# DICIONÁRIO: {} → dicionário (pares chave: valor)
# --------------------------------------------------------
# Inserir: dict[chave] = valor, update()
# Remover: pop(), del, clear()
# Editar: dict[chave] = novo_valor
# Observações: mutável, chaves únicas, pares chave:valor
dict = {"chave": "valor"}
# Criando um dicionário
print()  # só para pular linha
dicionario = {"nome": "Python", "nota": 10, "ativo": True}
print("dicionario:", dicionario)

# Inserindo/Atualizando elementos
dicionario["referencia"] = "w3s"  # adiciona nova chave
dicionario["site"] = (
    "https://www.w3schools.com/python/python_tuples.asp"  # atualiza valor existente
)
print("dicionario atualizado:", dicionario)

# Removendo elementos
valor_removido = dicionario.pop("ativo")  # remove chave e retorna valor
print("Removido 'ativo':", valor_removido)
del dicionario["referencia"]  # remove chave
print("dicionario final:", dicionario)

# ========================================================

# lista=[ string| number | Boolean | set | tupla       |      dict        ]
lista = ["string", 100, True, {"set"}, ("string", 100), {"chave": "valor"}]
print()  # só para pular linha
print(lista)  # imprime a lista inteira
print(lista[-1])  # acesso ao ultimo item desta lista (dicionário)
print(lista[4][0])  # acesso ao primeiro item da tupla dentro desta lista


conjunto = {"string", 100, True}
print("conjunto: ", conjunto)

conjunto2 = {"string", 100, True}
conjunto2.add("string")  # Elemento já existente não altera o conjunto
conjunto2.add(101)  # Adiciona novo elemento
print("conjunto2: ", conjunto2)  # Saída não imprime duplicadas
