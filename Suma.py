import matplotlib.pyplot as plt

entrada = input("Ingresa una serie de números separados por comas: ")
numeros = [int(x) for x in entrada.split(',')]
suma_acumulativa = [sum(numeros[:i+1]) for i in range(len(numeros))]

plt.bar(range(1, len(numeros) + 1), suma_acumulativa)
plt.xlabel('Número de elementos')
plt.ylabel('Suma acumulativa')
plt.title('Suma Acumulativa de la Serie de Números (Gráfico de Barras)')
plt.grid(True)
plt.show()