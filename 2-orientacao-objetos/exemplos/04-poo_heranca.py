class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def showInfos(self):
        print("Infomações do Veículo")
        print(self.marca, "/", self.modelo)


# ___________________________________
print(50 * "-")
c = veiculo("BYD", "SONG PRO")
c.showInfos()

# ___________________________________
print(50 * "-")


class Carro(veiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

    def showInfos(self):
        msg = "Infomações da classe Carro - Usando Herança da classe Veículo"
        msg2 = "\n" + self.marca + " / " + self.modelo
        print(msg, msg2)

        # # Exemplo sem reescrever o método:
        # # descomentar a próxima linha para usar e comenatar as linhs 25, 26 e 27
        # return super().showInfos()


c1 = Carro("Nissan", "Tiida")
c1.showInfos()

# ___________________________________
print(50 * "-")
