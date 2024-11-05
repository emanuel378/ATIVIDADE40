"""Faça um programa que crie uma matriz aleatoriamente.
O tamanho da matriz deve ser informado pelo usuário."""

from random import randint
linhas = int(input("Digite o número de linhas da matriz: "))
colunas = int(input("Digite o número de colunas da matriz: "))

    
matriz_aleatoria = []
for i in range(linhas):
        linha = []
        for j in range(colunas):
 # Preenche a linha com um número aleatório entre 0 e 9 
            linha.append(randint(0, 9))
        matriz_aleatoria.append(linha)

    
print("O computador fez essa matriz:")
for linha in matriz_aleatoria:
        print(linha)
