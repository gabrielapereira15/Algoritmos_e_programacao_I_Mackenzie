#atualiza_preco(valor): a função deve receber como parâmetro o preço de um produto,
#calcular e retornar o preço com aumento de 10%

def atualiza_preco(valor):

    precoatualizado = valor + (valor * 0.1)
    print("O preço com o aumento de 10% é:", precoatualizado)

atualiza_preco(1000)