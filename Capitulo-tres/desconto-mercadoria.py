preco_mercadoria = float(input("Qual o valor da mercadoria? "))
desconto_mercadoria = float(input("De quanto será o desconto (em %)? "))

valor_desconto = (preco_mercadoria * desconto_mercadoria) / 100 

novo_preco = preco_mercadoria - valor_desconto

print(f"O novo preço com desconto é: R$ {novo_preco:.2f}")
