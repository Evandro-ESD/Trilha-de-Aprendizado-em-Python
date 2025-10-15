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


#  Metodo construtor __init__()
class Person:
    def __init__(self, name, age):
        self.name = name  #
        self.age = age


# descomentar o método __str__() para ver a saída
#  def __str__(self):
#      return f"{self.name} - {self.age}"


p1 = Person("Evandro", 37)
print("Nome da classe p1 e o endereço na memória:", p1)
print(f"Olá meu nome é {p1.name} tenho {p1.age} anos e estou aprendendo Python!")
