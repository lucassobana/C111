import numpy as np

#1
np.random.seed(5)
array_floats = np.random.rand(10) * 2 - 1  # Array com 10 elementos entre -1 e 1
array_inteiros = np.floor(array_floats * 100)  # Multiplica por 100 e arredonda para baixo
print("Array floats:", array_floats)
print("\nArray inteiros:", array_inteiros)
print("--------------------")

#2
np.random.seed(10)
matriz = np.random.randint(1, 50, size=(4, 4))
print("Matriz:")
print(matriz)
print("--------------------")

#3
med_linhas = np.mean(matriz, axis=1)
med_colunas = np.mean(matriz, axis=0)
print("Media das linhas:", med_linhas)
print("Media das colunas:", med_colunas)
print("--------------------")

maior_media_linhas = np.max(med_linhas)
maior_media_colunas = np.max(med_colunas)
print("Maior media das linhas:", maior_media_linhas)
print("Maior media das colunas:", maior_media_colunas)
print("--------------------")

#4
valores, contagens = np.unique(matriz, return_counts=True)
aparicoes = dict(zip(valores, contagens))
print("Quantidade de aparicoes de cada numero na matriz:")
print(aparicoes)

print("\nNumeros que aparecem 2x:")
for numero, quantidade in aparicoes.items():
    if quantidade == 2:
        print(numero)
