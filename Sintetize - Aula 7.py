#Faça um programa em Python que leia 10 números inteiros e armazene-os em um vetor.
#Armazene os números positivos no vetor POSITIVO e os números negativos no vetor NEGATIVO.
#Mostre os vetores gerados.

positivos = []
negativos = []

i = 1
total_numeros = 10

while i <= total_numeros:
    numero_digitado = int(input("Digite o número {} de {}: ".format(i, total_numeros)))
    if numero_digitado >= 0:
        positivos.append(numero_digitado)
    else:
        negativos.append(numero_digitado)
    i = i + 1

print("Números positivos:", positivos)
print("Números negativos:", negativos)

