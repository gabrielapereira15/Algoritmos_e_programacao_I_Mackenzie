#Uma empresa fez uma pesquisa de mercado para saber se as pessoas gostaram ou não de um novo produto lançado no mercado.
#Para isso, forneceu o sexo do entrevistado (F - Feminino ou M - Masculino) e sua reposta (S - Sim ou N - Não).
#Sabe-se que foram entrevistadas dez pessoas. Faça um programa que calcule e mostre:
#Número de pessoas que respondeu “Sim”.
#Número de pessoas que respondeu “Não”.
#Número de mulheres que respondeu “Sim”.
#Percentagem de homens que respondeu “Não” entre todos os homens analisados.

print("** Bem-vindo ao Sistema de Pesquisa de Mercado **")
print("**** Para iniciar, insira os dados coletados ****")

# COLETA DOS DADOS

qntd_entevistado = 10
inicio = 1
feminino = []
masculino = []

while inicio <= qntd_entevistado:
    sexo = (input("ENTREVISTADO {} DE {} - Qual o sexo do entrevistado? Digite F - Feminino ou M - Masculino: ".format(inicio, qntd_entevistado)))
    sexo = sexo.upper()
    if sexo == "M":
        masculino.append(input("Gostou do novo produto lançado? Digite S -  SIM ou N - Não: "))
    elif sexo == "F":
        feminino.append(input("Gostou do novo produto lançado? Digite S -  SIM ou N - Não: "))
    inicio = inicio + 1

# RESPOSTAS SIM

resposta_sim = []

for fem_sim in feminino:
    if fem_sim == "s":
        resposta_sim.append(fem_sim)

for masc_sim in masculino:
    if masc_sim == "s":
        resposta_sim.append(masc_sim)

print("A quantidade de pessoas que respondeu SIM foi: ", len(resposta_sim))

# RESPOSTAS NÃO

resposta_nao = []

for fem_nao in feminino:
    if fem_nao == "n":
        resposta_nao.append(fem_nao)

for masc_nao in masculino:
    if masc_nao == "n":
        resposta_nao.append(masc_nao)

print("A quantidade de pessoas que respondeu NÃO foi: ", len(resposta_nao))

# MULHERES QUE RESPONDERAM SIM

mulheres_sim = 0
for fem_sim in feminino:
    if fem_sim == "s":
        mulheres_sim += 1

print("A quantidade de mulheres que respondeu SIM foi: ", mulheres_sim)

# PORCENTAGEM DE HOMENS QUE RESPONDERAM NÃO

homens_nao = 0
for masc_nao in masculino:
    if masc_nao == "n":
        homens_nao += 1

porcentagem = (100 / len(masculino)) * homens_nao

print("A porcentagem de homens que respondeu NÃO foi:", porcentagem,"%")