#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
#Imprima os três vetores.

numeros = []
total_numeros = 20
num_inicial = 1

while num_inicial <= total_numeros:
    numeros.append(int(input("Digite o número {} de {}: ".format(num_inicial, total_numeros))))
    num_inicial = num_inicial + 1

pares = []
impares = []
i = 0
posic_inicial = 0

while i < total_numeros:
    if numeros[posic_inicial] % 2 == 0:
        pares.append(numeros[posic_inicial])
    else:
        impares.append(numeros[posic_inicial])
    posic_inicial = posic_inicial + 1
    i = i + 1

print("Os números digitados foram:", numeros)
print("Os número pares são:", pares)
print("Os números ímpares são:", impares)