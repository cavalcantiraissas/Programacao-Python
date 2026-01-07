deposito_poupanca = float(input("Quanto você gostaria de depositar?: "))
taxa_juros = float(input("Qual valor da tada de juros? "))

valor_inicial = deposito_poupanca
contador = 1

while contador <= 24:
    deposito_poupanca = deposito_poupanca + (deposito_poupanca * (taxa_juros / 100))
    print(f"Mês: {contador} | Valor Total: {deposito_poupanca:.2f}")
    contador = contador + 1
lucro = deposito_poupanca - valor_inicial
print(f"Você depositou inicialmente {valor_inicial} e, após 24 meses, você resgata {deposito_poupanca:.2f}, resultando em um lucro de {lucro:.2f}")
