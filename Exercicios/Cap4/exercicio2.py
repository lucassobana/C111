import numpy as np

#1
array_linear = np.linspace(0, 1, 21)
print(array_linear)
print("-------------------------------------------------")

#2
array_0_51 = np.arange(0, 51, 2)

array_100_50 = np.arange(100, 50, -2)

array_concatenado = np.concatenate((array_0_51, array_100_50))

array_ordenado = np.sort(array_concatenado)

print(array_ordenado)
print("-------------------------------------------------")

#3
array_decrescente = np.sort(array_concatenado)[::-1]

print(array_decrescente)
print("-------------------------------------------------")

#4
matriz_3x4 = np.ones((3, 4))

# Transformar a matriz em um array 1-D
array_1d = matriz_3x4.flatten()

# Mostrar o resultado
print("Array 1-D:")
print(array_1d)
print("-------------------------------------------------")

#5
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Obter o número de linhas e colunas da matriz
num_linhas, num_colunas = matriz.shape

# Multiplicar o número de linhas pelo número de colunas
total_elementos = num_linhas * num_colunas

# Verificar se o total de elementos é par ou ímpar
if total_elementos % 2 == 0:
    print("A matriz poderia se tornar um vetor com um numero par de elementos.")
else:
    print("A matriz poderia se tornar um vetor com um numero impar de elementos.")
