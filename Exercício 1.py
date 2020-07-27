#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

numeros = []
numero_atual = 1
total_numeros = 5

while numero_atual <= total_numeros:
    numeros.append(int(input("Digite o número {} de {}:".format(numero_atual, total_numeros))))
    numero_atual = numero_atual + 1

print("A sequência de números é: ", numeros)
