#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
quantidade_notas = 1
total_notas = 4

while quantidade_notas <= total_notas:
    notas.append(float(input("Informe a nota {} de {}: ".format(quantidade_notas,total_notas))))
    quantidade_notas = quantidade_notas + 1

quantidade_notas = len(notas)
soma_notas = sum(notas)
media = soma_notas / quantidade_notas

print("As suas notas foram:", notas)
print("A sua média é:", media)
