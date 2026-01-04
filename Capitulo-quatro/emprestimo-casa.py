valor_casa = float(input("Qual o valor da casa?:\n"))
salario_interessado = float(input("Quanto você recebe?:\n"))
anos_pagamento = int(input("Em quantos anos você deseja pagar a casa?:\n"))

conversao_anos = anos_pagamento * 12 
valor_prestacao = valor_casa / conversao_anos

trinta_porcento_salario = (salario_interessado * 30)/ 100

if valor_prestacao > trinta_porcento_salario:
    print("Infelizmente, não aprovamos o empréstimo.")
else:
    print("O seu empréstimo foi aprovado.")
