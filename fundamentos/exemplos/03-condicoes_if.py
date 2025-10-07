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

# ================ MENOR QUE ( < )================ #
# Se o número armazenado na varável 'b' for menor que o número da variável 'a', ele imprime uma mensagem na tela dizendo isso.
# if b < a (Por extenso: se b for maior que a imprima Variável b = 30 é menor que a variável a = 17)
a = 17
b = 30
if b < a:
    print(f"Variável b = {b} é menor que a variável a = {a} ")

# ================ MENOR OU IGUAL ( <= )================ #
# Se o número armazenado na variável 'a' for menor ou igual ao número da variável 'b',
# ele imprime uma mensagem na tela dizendo isso.
# if a <= b (Por extenso: se a for menor ou igual a b imprima Variável a = 17 é menor ou igual à variável b = 30)
a = 17
b = 30
if a <= b:
    print(f"Variável a = {a} é menor ou igual à variável b = {b}")


# ================ MAIOR QUE ( > )================ #
# Se o número armazenado na varável 'b' for maior que o número da variável 'a', ele imprime uma mensagem na tela dizendo isso.
# if b > a (Por extenso: se b for maior que a imprima Variável b = 30 é maior que a variável a = 17 )
a = 17
b = 30
if b > a:
    print(f"Variável b = {b} é maior que a variável a = {a} ")

# ================ MAIOR OU IGUAL ( >= )================ #
# Se o número armazenado na variável 'b' for maior ou igual ao número da variável 'a',
# ele imprime uma mensagem na tela dizendo isso.
# if b >= a (Por extenso: se b for maior ou igual a a imprima Variável b = 30 é maior ou igual à variável a = 17)
a = 17
b = 30
if b >= a:
    print(f"Variável b = {b} é maior ou igual à variável a = {a}")


# ================ not ( Lógico )================ #
# O operador 'not' inverte o resultado lógico de uma condição.
# Se a condição "a == b" for falsa, 'not (a == b)' será verdadeira.
# if not (a == b) (Por extenso: se não for verdade que a é igual a b, então imprima...)
a = 17
b = 30
if not (a == b):
    print(f"Não é verdade que a = {a} é igual a b = {b}")

# ================ and ( Lógico )================ #
# O operador 'and' exige que as duas condições sejam verdadeiras ao mesmo tempo.
# if a < b and b > 10 (Por extenso: se a for menor que b e b for maior que 10, então imprima...)
a = 17
b = 30
if a < b and b > 10:
    print(
        f"As duas condições são verdadeiras: a = {a} é menor que b = {b}, e b é maior que 10"
    )


# ================ and ( Lógico )================ #
# O operador 'or' exige que pelo menos uma condição seja verdadeira.
# if a > b or b > 10 (Por extenso: se a for maior que b ou b for maior que 10, então imprima...)
a = 17
b = 30
if a > b or b > 10:
    print(f"Pelo menos uma das condições é verdadeira: (a > b) ou (b > 10)")
