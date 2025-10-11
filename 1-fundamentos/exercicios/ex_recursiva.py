# # 1️⃣ Fatorial básico (recursivo)
# # Enunciado:
# # Escreva uma função recursiva que receba um número inteiro n e retorne n!.
# # Use o caso base corretamente.
# # Extra: Imprima os valores parciais para entender a recursão.


# def fatorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         print(n)
#         return n * (fatorial(n - 1))


# print(fatorial(5))


# # 2️⃣ Fatorial iterativo
# # Enunciado:
# # Escreva uma função usando laço for que calcule o fatorial de um número n.
# # Compare o resultado com uma versão recursiva.
# def for_fatorial(n):
#     resultado = 1
#     iterativo = [resultado]
#     for i in range(1, n + 1):
#         resultado *= i
#         iterativo.append(resultado)

#     return resultado, iterativo


# res, passos = for_fatorial(5)
# print("Fatorial:", res)
# print("Passos:", passos)
# print(40 * "*")


# # Soma dos fatoriais parciais
# # Enunciado:
# # Crie uma função recursiva que, além de calcular n!, retorne a soma de todos os resultados parciais da recursão.
# # Exemplo:
# # •	Para n = 5, os resultados parciais seriam: 1, 2, 6, 24, 120
# # •	Soma: 1 + 2 + 6 + 24 + 120 = 153


# def soma_fatorial(n):
#     if n == 1 or n == 0:
#         return 1, 1  # (fatorial, soma_parciais)
#     else:
#         fat_anterior, soma_anterior = soma_fatorial(n - 1)
#         fat_atual = n * fat_anterior
#         soma_total = soma_anterior + fat_atual
#         return fat_atual, soma_total


# try:
#     resultado_fatorial, soma_parciais = soma_fatorial(5)
#     print(f"Fatorial: {resultado_fatorial}")
#     print(f"Soma dos Fatoriais Parciais: {soma_parciais}")
# except Exception as erro:
#     print(erro)

print(40 * "*")
# Fatorial com validação de entrada
# Enunciado:
# Modifique sua função de fatorial para verificar se o número é inteiro não negativo.
# •	Se não for, lance uma exceção (ValueError).
# •	Use try/except para testar a função com entradas inválidas.


def fatorial_com_validação_de_entrada(n):
    if n < 0:
        raise ValueError(
            "O fatorial de um número negativo não existe."
            "\nEssa operação não pode ser realizada com números negativos.."
        )
    if n == 1 or n == 0:
        return 1, 1
    else:
        fat_anterior, soma_anterior = fatorial_com_validação_de_entrada(n - 1)
        fat_atual = n * fat_anterior
        soma_total = soma_anterior + fat_atual

        return fat_atual, soma_total


try:
    fatorial, soma = fatorial_com_validação_de_entrada(5)
    print(f"Fatorial: {fatorial}")
    print(f"Soma dos parciais: {soma}")
except ValueError as e:
    print("Erro capturado:", e)
