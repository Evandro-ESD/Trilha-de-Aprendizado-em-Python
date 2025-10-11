#  _____________________________________________________________________________
# |                          |    Operator	   |    Example	     |   Same As    |
# |                          |    Operador     |    Exemplo      |   Igual a    |
# |__________________________|_________________________________________________ |
# |  Atribuição              |    = 	       |    x = 5	     |   x = 5	    |
# |  Soma e atribuição       |    +=	       |    += 3	     |   x = x + 3  |
# |  Subtração e atrib       |    -=	       |    -= 3	     |   x = x - 3  |
# |  Multiplicação e atrib   |    *=	       |    *= 3	     |   x = x * 3  |
# |  Divisão e atribuição    |    /=	       |    /= 3	     |   x = x / 3  |
# |  Resto da divisão        |    %=	       |    %= 3	     |   x = x % 3  |
# |  Divisão inteira e atrib |    //=	       |    //= 3        |   x = x // 3	|
# |  Exponenciação e atrib.  |    **=	       |    **= 3	     |   x = x ** 3	|
# |  AND bit a bit e atrib   |    &=	       |    &= 3	     |   x = x & 3	|
# |  OR bit a bit e atrib.   |    |=	       |    |= 3	     |   x = x | 3	|
# |  XOR bit a bit e atrib   |    ^=	       |    ^= 3	     |   x = x ^ 3	|
# |  Deslocamento à direita  |    >>=	       |    x >>= 3	     |   x = x >> 3	|
# |  Deslocamento à esquerda |    <<=	       |    x <<= 3	     |   x = x << 3	|
# |  Operador Walrus         |    :=	       |    print(x := 3)|   x = 3      |
# |__________________________|__________________________________________________|


print(40 * "--")
x = 10
print(
    f"Operador de atribuição '=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")
# print("\n")

print(40 * "--")
x = 6  # primera atribuição: x recebe 6
x += 3  # segunda atribuição: soma 3 ao valor atual de x ( x = x + 3 )
print(
    f"Operador de atribuição '+=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")
# print("\n")

print(40 * "--")
x = 6  # primera atribuição: x recebe 6
x -= 3  # segunda atribuição: subtrai 3 ao valor atual de x ( x = x - 3 )
print(
    f"Operador de atribuição '-=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
x = 6  # primera atribuição: x recebe 6
x *= 3  # segunda atribuição: multiplica 3 ao valor atual de x ( x = x * 3 )
print(
    f"Operador de atribuição '*=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
x = 6  # primera atribuição: x recebe 6
x /= 3  # segunda atribuição: divide 3 ao valor atual de x ( x = x / 3 )
print(
    f"Operador de atribuição '/=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
x = 7  # primera atribuição: x recebe 6
x //= 3  # segunda atribuição: divide 3 ao valor atual de x ( x = x // 3 )
print(
    f"Operador de atribuição '//=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")
# Observação em python /= retorna (mostra) ponto flutuante mesmo para números inteiros
# enquanto //= retorna (mostra) divisão inteira

print(40 * "--")
x = 7  # primera atribuição: x recebe 6
x %= 3  # segunda atribuição: divide 3 ao valor atual de x ( x = x % 3 )
#    7 |_3_   ← dividendo | divisor
#    1   2    ← Quociente → número de vezes que 3 cabe em 7
#      1    ← resto, sobra da divisão (7 - 6)

print(
    f"Operador de atribuição '%=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")
# O operador %= retorna o resto da divisão ( 7 / 3 = 1)
# '%'com inteiros retorna inteiro

print(40 * "--")
# Operador de divisão inteira com atribuição
x = 7  # primeira atribuição: x recebe 7
x //= 3  # segunda atribuição: x recebe a divisão inteira de x por 3
print(
    f"Operador de atribuição '//=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
# Operador de exponenciação com atribuição
x = 2
x **= 3  # x = x ** 3 (2 elevado a 3)
print(
    f"Operador de atribuição '**=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
# Operador AND bit a bit com atribuição
x = 6  # binário: 110
x &= 3  # x = x & 3 → 110 & 011 = 010 (2)
print(
    f"Operador de atribuição '&=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
# Operador OR bit a bit com atribuição
x = 2  # binário: 010
x |= 3  # x = x | 3 → 010 | 011 = 011 (3)
print(
    f"Operador de atribuição '|=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
# Operador XOR bit a bit com atribuição
x = 3  # binário: 011
x ^= 1  # x = x ^ 1 → 011 ^ 001 = 010 (2)
print(
    f"Operador de atribuição '^=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
# Operador deslocamento à direita com atribuição
x = 16  # binário: 10000
x >>= 2  # desloca 2 bits para a direita → 100 (4)
print(
    f"Operador de atribuição '>>=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
# Operador deslocamento à esquerda com atribuição
x = 4  # binário: 100
x <<= 2  # desloca 2 bits para a esquerda → 10000 (16)
print(
    f"Operador de atribuição '<<=' | Valor de 'x': {x} | Tipo: {type(x)} | {isinstance(x, int)}"
)
print(40 * "--")

print(40 * "--")
# Operador de expressão (walrus operator) - atribuição dentro de expressão
# Disponível no Python 3.8+
if (y := 5) > 2:  # atribui 5 a y e compara com 2
    print(f"Operador ':=' | Valor de 'y': {y} | Tipo: {type(y)} | {isinstance(y, int)}")
print(40 * "--")
# Sem walrus operator
# y = 5
# if y > 2:
#     print(y)

# numeros = [1, 2, 3, 4]     #| Itera sobre lista  |
# while (n := len(numeros)): #| atribui n=4,3,2,1, |
#    numeros.pop()
#    print(numeros)
# print(numeros)

# if (y := 5) > 2:          # | Atribui y=5 e      |
# print(y)               #| compara 5>2 → True
