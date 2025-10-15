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


class Veiculo:
    marca = "Chevrolet"
    modelo = "Celta"


v1 = Veiculo()
print(v1.marca)  #
