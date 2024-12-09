import numpy as np

# Criando uma matriz 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Matriz Original:")
print(matriz) 
for i in range(matriz.shape[0]): #Itera sobre o número de linhas na matriz
    for j in range(matriz.shape[1]): #Itera sobre o número de colunas na matriz
        print(matriz[i, j])
