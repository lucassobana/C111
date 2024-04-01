import numpy as np

arr = np.loadtxt('space.csv', delimiter=';',dtype=str,encoding='utf-8')

#1
missao = arr[1:,7]
missao_sucesso = len(missao[np.char.find(missao,'Success') == 0])
print(missao_sucesso/len(missao)*100)
print('-------------------')

#2
gastos = arr[1:,6].astype(float)
print(sum(gastos[gastos>0])/len(gastos[gastos>0]))
print('-------------------')

3
cidades = arr[1:,2]
usa = np.char.find(cidades,'USA') > 0
print(len(cidades[usa]))
print('-------------------')

4
empresas,gastos = arr[1:,1],arr[1:,6].astype(float)
missao_cara = np.where(empresas == 'SpaceX')
print(max(gastos[missao_cara]))
print('-------------------')

#5
empresas, num_missoes = np.unique(arr[1:,1], return_counts= True)

for i in range(len(empresas)):
    print(empresas[i],num_missoes[i])