# Condições Python e instruções If

#  _____________________________
# |   COMPARAÇÃO      | SÍMBOLO |
# |___________________|_________|
# |  igualdade        |   ==    |
# |  Diferente de     |   !=    |
# |  Menor que        |   <     |
# |  Menor ou igual   |   <=    |
# |  Maior que        |   >     |
# |  Maior ou igual   |   >=    |
# |  not (lógico)     |   not   |
# |  and (lógico)     |   and   |
# |  or (lógico)      |   or    |
#  ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨


# ------------ Exemplos práticos ------------ #

# ================ IGUALDADE ( == )================ #
# Se o número armazenado na variável 'a' for igual ao número da variável 'b',
# ele imprime uma mensagem na tela dizendo isso.
# if a == b (Por extenso: se a for igual a b imprima Variável a = 17 é igual à variável b = 30)

a = 17
b = 30
if a == b:
    print(f"Variável a = {a} é igual à variável b = {b}")

# ================ DIFERENTE DE ( != )================ #

# Se o número armazenado na variável 'a' for diferente do número da variável 'b',
# ele imprime uma mensagem na tela dizendo isso.
# if a != b (Por extenso: se a for diferente de b imprima Variável a = 17 é diferente da variável b = 30)

a = 17
b = 30
if a != b:
    print(f"Variável a = {a} é diferente da variável b = {b}")


# ================ MAIOR QUE ( > )================ #
# Se o número armazenado na varável 'b' for maior que o número da variável 'a', ele imprime uma mensagem na tela dizendo isso.
# if b > a (Por extenso: se b for maior que a imprima Variável b = 30 é maior que a variável a = 17 )

a = 17
b = 30
if b > a:
    print(f"Variável b = {b} é maior que a variável a = {a} ")

# ================ MENOR QUE ( < )================ #
# Se o número armazenado na varável 'b' for menor que o número da variável 'a', ele imprime uma mensagem na tela dizendo isso.
# if b < a (Por extenso: se b for maior que a imprima Variável b = 30 é menor que a variável a = 17)
a = 17
b = 30
if b < a:
    print(f"Variável b = {b} é menor que a variável a = {a} ")
