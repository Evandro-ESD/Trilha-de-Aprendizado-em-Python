# Exemplo: Tratamento de Erros

try:
    variavel_string = "string"
    variavel_string += 1
    print(variavel_string)

except Exception as erro:
    print(
        "Erro manual: \nNão é permitido concatenar string com inteiro, somente string com string\n"
    )
    print("Erro capturado pelo Exception:\n", erro)
