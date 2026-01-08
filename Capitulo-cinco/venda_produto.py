valor_total = 0
quantidade_de_produtos = None
while True:
    codigo_do_produto = int(input("Digite o Código do Produto: "))
    if codigo_do_produto == 0:
        print(f"Valor total das compras: R$ {valor_total}\n")
        break
    if codigo_do_produto == 1:
        quantidade_de_produtos = int(input("Quantos produtos você deseja adicionar?: "))
        valor_total = valor_total + (0.50 * quantidade_de_produtos)
    elif codigo_do_produto == 2:
        quantidade_de_produtos = int(input("Quantos produtos você deseja adicionar?: "))
        valor_total = valor_total + (1.00 * quantidade_de_produtos)
    elif codigo_do_produto == 3:
        quantidade_de_produtos = int(input("Quantos produtos você deseja adicionar?: "))
        valor_total = valor_total + (4.00 * quantidade_de_produtos)
    elif codigo_do_produto == 5:
        quantidade_de_produtos = int(input("Quantos produtos você deseja adicionar?: "))        
        valor_total = valor_total + (7.00 * quantidade_de_produtos)
    elif codigo_do_produto == 9:
        valor_total = valor_total + (8.00 * quantidade_de_produtos)
    else:
        print("Código Inválido!\n")
