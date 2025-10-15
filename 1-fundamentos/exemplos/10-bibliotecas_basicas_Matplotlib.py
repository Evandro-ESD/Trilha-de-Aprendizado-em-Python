# # Exemplo: Bibliotecas Básicas

# -----  Matplotlib ----- #

# Exemplo: Gráfico de linha com Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Criando dados com NumPy
x = np.linspace(0, 10, 100)  # 100 pontos entre 0 e 10
y = np.sin(x)  # Função seno
y2 = np.cos(x)  # Função cosseno

# Criando o gráfico
plt.figure(figsize=(10, 5))  # Tamanho do gráfico
plt.plot(x, y, label="Seno", color="blue", linestyle="-")
plt.plot(x, y2, label="Cosseno", color="red", linestyle="--")

# Personalizando
plt.title("Gráfico de Seno e Cosseno")  # Título
plt.xlabel("Eixo X")  # Nome do eixo X
plt.ylabel("Eixo Y")  # Nome do eixo Y
plt.legend()  # Legenda
plt.grid(True)  # Grade no fundo

# Exibindo o gráfico
plt.show()
