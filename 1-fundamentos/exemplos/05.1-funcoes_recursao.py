# |Referencia: https://www.w3schools.com/python/python_functions.asp

##################################################
##################################################
#######                                    #######
#######             Recursão               #######
#######                                    #######
##################################################
##################################################


"""
Recursão é quando uma função chama a si mesma para resolver um problema dividindo-o em partes menores.
É muito usada em matemática e algoritmos (como fatoriais, somas e percursos de estruturas).

Pontos principais:

Permite repetir uma tarefa dentro da própria função.

Precisa ter uma condição de parada — caso contrário, entra em loop infinito e causa erro de memória.

Quando bem escrita, é uma forma elegante e eficiente de resolver problemas.
"""


########################################################


def fatorial(n):
    if n == 0 or n == 1:
        return 1  # caso base para
    else:
        fat = fatorial(n - 1)
        res = n * fat  # chamada recursiva >> n * fatorial(n - 1) <<
        print(25 * "_")
        print(f"Calculando fatorial({n - 1})")
        print(f"{n} * {fat} = {res}")
        return res


print(f"O fatorial é: {fatorial(5)}")
