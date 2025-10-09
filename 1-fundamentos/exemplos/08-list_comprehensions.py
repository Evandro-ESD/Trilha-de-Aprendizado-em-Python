# Exemplo: List Comprehensions
# Referência: leandrohirt.oficial instagram

produtos = [
    {"nome": "celular", "vendas": 230},
    {"nome": "Notebook", "vendas": 188},
    {"nome": "Tablet", "vendas": 75},
    {"nome": "Smartwath", "vendas": 95},
    {"nome": "Fone de ouvido", "vendas": 310},
]

mais_vendidos = [produto["nome"] for produto in produtos if produto["vendas"] > 300]

print()
print(mais_vendidos)

# ================================================
mais_vendidos_so_o_nome = next(
    (produto["nome"] for produto in produtos if produto["vendas"] > 300), None
)

print(mais_vendidos_so_o_nome)
print(40 * "-")
# _________________________________________

# List Comprehension
# Compreensão de listas

# [ expressão for item in iterável ]

# [ expressão for item in iterável if condição ]

# _________________________#

"""
l1 = [1, 2, 3]
l2 = [2, 2, 2]

distributiva = [ k * m for k in l1 for m in l2 ]

l3 = []
for i in l1:
	for k in l2:
		l3.append(i * k)
		
print(l3)
print(distributiva)
"""
pares = [x for x in range(10) if x % 2 == 0]

print("Números pares de 0 a 9: ", pares)

impares = [x for x in range(10) if x % 2 == 1]

print("Números ímpares de 0 a 9: ", impares)

frase = "Estudando Python todos os dias. A lógica é apenas o principio da sabedoria e não o fim"

vogais = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]

letters = [l for l in frase.lower() if l == "a" or l == "e" or l == "o"]

print("Quantas letras 'a', 'e' e 'o' têm na frase", len(letters))

so_vogais = [v for v in frase if v in vogais]

print(f"A frase tem {len(frase)} letras e {len(so_vogais)} vogais acentuadas ou não")
