#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
#Imprima as consoantes.

caracteres = []
vogais = ["a", "e", "i", "o", "u"]
carac_atual = 1
total_carac = 10

while carac_atual <= total_carac:
    caracteres.append(input("Digite o caractere {} de {}:".format(carac_atual, total_carac)))
    carac_atual = carac_atual + 1

pos_caracter = 0
qtd_consoantes = 0
consoantes = []

while pos_caracter < total_carac:
    if caracteres[pos_caracter] not in vogais:
        consoantes.append(caracteres[pos_caracter])
        qtd_consoantes = qtd_consoantes + 1

    pos_caracter = pos_caracter + 1

print("A quantidade de consoantes digitadas foi:", qtd_consoantes)
print("As consoantes são:", consoantes)