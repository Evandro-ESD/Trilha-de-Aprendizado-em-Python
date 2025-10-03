# Exercício: Calculadora


class Calculadora:
    def __init__(self):
        self.num1 = int(input("Insira o 1º número: "))
        self.operacao = input('Insira a operação ( "+" | "-" | "*" | "/" ): ')
        self.num2 = int(input("Insira o 1º número: "))

    def calculo(self):
        match self.operacao:
            case "+":
                return self.num1 + self.num2
            case "-":
                return self.num1 - self.num2
            case "*":
                return self.num1 * self.num2
            case "/":
                return (
                    "Erro: divisão por zero!"
                    if self.num2 == 0
                    else self.num1 / self.num2
                )
            case _:
                return "Operação invalida!"


calc = Calculadora()
print("Resulatdo: ", calc.calculo())
