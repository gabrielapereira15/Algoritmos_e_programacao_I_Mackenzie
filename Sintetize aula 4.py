saldomedio = float (input("Digite o saldo médio do último ano:"))
if saldomedio <= 200:
    credconcedido = (saldomedio * 0.1)
    print ("Seu saldo médio é: %.1f" %saldomedio)
    print ("O crédito concedido será: %.1f" %credconcedido)
elif saldomedio >= 200.01 and saldomedio <= 300:
    credconcedido = (saldomedio * 0.2)
    print ("Seu saldo médio é: %.1f" %saldomedio)
    print ("O crédito concedido será: %.1f" %credconcedido)
elif saldomedio >= 300.01 and saldomedio <= 400:
    credconcedido = (saldomedio * 0.25)
    print ("Seu saldo médio é: %.1f" %saldomedio)
    print ("O crédito concedido será: %.1f" %credconcedido)
elif saldomedio >= 400.01:
    credconcedido = (saldomedio * 0.3)
    print ("Seu saldo médio é: %.1f" %saldomedio)
    print ("O crédito concedido será: %.1f" %credconcedido)
    
