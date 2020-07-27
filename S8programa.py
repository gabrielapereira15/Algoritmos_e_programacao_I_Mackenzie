#atualiza_preco(valor): a função deve receber como parâmetro o preço de um produto,
#calcular e retornar o preço com aumento de 10%

#taxa(valor): a função calcula e retorna a taxa de 2.5% sobre o preço do produto atualizado.

#o programa principal que deve solicitar ao usuário o preço do produto,
#chamar as funções atualiza_preco e taxa. Apresente os valores calculados no programa principal.

preco_produto = float(input("Digite o preço do produto:"))

def atualiza_preco(valor):
    valor_atualizado = valor + (valor * 0.1)
    return valor_atualizado

def taxa():
    valor_taxa = atualiza_preco(preco_produto) * 0.025
    return valor_taxa

print("O valor do produto com o aumento de 10% é:", atualiza_preco(preco_produto))
print("O valor da taxa é:", taxa())
