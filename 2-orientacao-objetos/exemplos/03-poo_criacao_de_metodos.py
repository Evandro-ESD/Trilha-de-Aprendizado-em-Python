##################################################
##################################################
#######                                    #######
#######        classes e objetos           #######
#######                                    #######
##################################################
##################################################

# Uma classe define a aparência de um objeto, e um objeto é criado com base nessa classe.
# Quando você cria um objeto de uma classe, ele herda todas as variáveis ​​e funções definidas dentro dessa classe.

# ["Toyota", "Volkswagen", "Chevrolet", "Fiat", "Ford", "Honda", "BMW", "Mercedes-Benz", "Hyundai", "Jeep", "Nissan", "Renault", "BYD", "Caoa Chery", "Peugeot", "Citroën", "Audi", "Land Rover", "Ferrari", "Porsche"]

# O parâmetro self é uma referência à instância atual da classe e é usado para acessar variáveis ​​que pertencem à classe.

# Pode ser qualquer nome, podemos chamá-lo como quiser, mas precisa ser o primeiro parâmetro de qualquer função na classe:


# Descomente para ver o resultado """ """
"""
class PersonTeste:
    def __init__(qualquerNome, name, age):
        qualquerNome.name = name
        qualquerNome.age = age


pTeste = PersonTeste("Nome de Teste", 37)
print(
    f"Olá meu nome é {pTeste.name} tenho {pTeste.age} anos e estou testando a substituição do parâmetro self em Python!"
)
"""


#  Metodo construtor __init__()
class Person:
    def __init__(self, name, age):
        self.name = name  #
        self.age = age

    def saudacao(self):
        print(
            f"Olá meu nome é {p1.name} tenho {p1.age} anos e estou aprendendo Python!"
        )


print(40 * "_")
p1 = Person("Evandro", 37)
p1.saudacao()
# ______________________________
print(40 * "_")
print("Modificando propriedades")
p1.age = 78  # atribui novo valor a propriedade age
p1.saudacao()

# ______________________________
print(40 * "_")
print("Excluindo propriedades")
del p1.age
try:
    p1.saudacao()
except Exception as erro:
    print("Erro:", erro)
    print("Erro: O objeto 'Pessoa' não possui o atributo 'idade'")  # tradução do erro

# ______________________________
print(40 * "_")
print("Excluindo propriedades")
del p1
try:
    p1.saudacao()
except Exception as erro:
    print("Erro:", erro)
