linguagens = ["python", "java", "javascript"]
linguagens2 = ["python", "java", "javascript"]
linguagens3 = linguagens


def identidadeIS(list1, list2):
   if list1 is list2:
      print("\nOs ojetos são o mesmo objeto na memória!")
   else: 
      print("\nOs ojetos não são o mesmo objeto, apenas têm valores iguais!")


def identidadeIS_not(list1, list2):
    if list1 is not list2:
        print(f"\nOs ojetos não são o mesmo objeto na memória!")
    else: 
        print("\nOs ojetos são o mesmo objeto na memória!")


def identidadeIgualdade(list1, list2):
    if list1 == list2:
        print("\nOs ojetos têm valores iguais!")
    else: 
        print("\nOs ojetos têm valores diferentes!")


print(45*"_")
print("Operador de identidade 'is'")
identidadeIS(linguagens, linguagens2)
identidadeIS(linguagens, linguagens3)
print(45*"_")

print(45*"*")
print("Operador de identidade 'is not'")
identidadeIS_not(linguagens, linguagens2)
identidadeIS_not(linguagens, linguagens3)
print(45*"_")

print(45*"_")
print("Operador de igualdade '=='")
identidadeIgualdade(linguagens, linguagens2)
identidadeIgualdade(linguagens, linguagens3)
print(45*"_")



