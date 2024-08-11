#Escreva um programa que crie uma lista de números inteiros aleatórios e, em seguida, imprima o maior e o menor número da lista. 

import random

numeros = [random.randint(1, 100) for _ in range(10)]

minimo = min(numeros)
maximo = max(numeros)

print (numeros)
print(f'Minímo: {minimo} e máximo: {maximo}')