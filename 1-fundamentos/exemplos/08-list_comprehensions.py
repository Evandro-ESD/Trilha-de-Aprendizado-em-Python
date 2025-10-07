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

print(mais_vendidos)

# ================================================
mais_vendidos_so_o_nome = next(
    (produto["nome"] for produto in produtos if produto["vendas"] > 300), None
)

print(mais_vendidos_so_o_nome)
