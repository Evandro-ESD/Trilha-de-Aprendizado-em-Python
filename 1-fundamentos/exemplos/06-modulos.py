# Exemplo: Módulos
"""
      Módulos em Python
Um módulo é um arquivo python que contém funções, variáveis, etc., e possui extensão .py. É simplesmente um arquivo python que pode ser importado para outro programa python. O nome do módulo é o nome do próprio arquivo python.

referência: https://pt.python-3.com/?p=2415
"""

#  Importação do arquivo 'modulo_para_exemplo'
import modulo_para_exemplo

# Chamada da função 'dobro' do módulo 'modulo_para_exemplo' passando o número 2
mod = modulo_para_exemplo.dobro(2)
print(mod)


# ______________________________________________________
# Importação de modulo padrão (nativo do python)
import math

# Chamada da função sqrt() do módulo math para calcular a raiz quadrada de 25
print(math.sqrt(25))

# ______________________________________________________
# Importação passando apelido "math as m" (math como m)
import math as m

# Usando o apelido
print(m.sqrt(25))

# ______________________________________________________
# Importação parcial permite importar apenas as funções necessárias
from math import sqrt, pow

# Como a função sqrt foi importada diretamente,
# não é necessário usar "math.sqrt" e "math.sqrt", basta chamar "sqrt" ou "pow" diretamente
print(sqrt(25))
print(pow(5, 2))
# ______________________________________________________
