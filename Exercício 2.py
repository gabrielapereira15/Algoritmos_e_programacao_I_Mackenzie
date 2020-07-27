#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

numeros = []
numero_atual = 1
total_numeros = 10

while numero_atual <= total_numeros:
    numeros.append((float(input("Digite o número {} de {}:".format(numero_atual, total_numeros)))))
    numero_atual = numero_atual + 1

numeros.sort(reverse = True)
print("A sequência de números na ordem inversa é: ", numeros)