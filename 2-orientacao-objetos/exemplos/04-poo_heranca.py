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
