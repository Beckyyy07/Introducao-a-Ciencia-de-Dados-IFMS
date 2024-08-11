'''
Escreva um programa que leia uma lista de números inteiros do usuário e exiba a soma de todos os números ímpares na lista.
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [i for i in numeros if i % 2 != 0]
soma = sum(impares)

print("Números ímpares:", impares)
print(soma)




