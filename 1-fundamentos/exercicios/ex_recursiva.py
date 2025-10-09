# 1️⃣ Fatorial básico (recursivo)
# Enunciado:
# Escreva uma função recursiva que receba um número inteiro n e retorne n!.
# Use o caso base corretamente.
# Extra: Imprima os valores parciais para entender a recursão.


def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        print(n)
        return n * (fatorial(n - 1))


print(fatorial(5))


# 2️⃣ Fatorial iterativo
# Enunciado:
# Escreva uma função usando laço for que calcule o fatorial de um número n.
# Compare o resultado com uma versão recursiva.
def for_fatorial(n):
    resultado = 1
    iterativo = [resultado]
    for i in range(1, n + 1):
        resultado *= i
        iterativo.append(resultado)

    return resultado, iterativo


res, passos = for_fatorial(5)
print("Fatorial:", res)
print("Passos:", passos)
