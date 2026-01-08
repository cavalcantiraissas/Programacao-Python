soma =0 
quantidade_de_numeros = 0
while True:
    numero = int(input("Digite um número a somar ou 0 para sair: "))
    if numero ==0:
        media_arit = soma / quantidade_de_numeros
        print(f"Você digitou: {quantidade_de_numeros} números \n A média aritmética dos valores que você digitou é: {media_arit} \n")
        break
    soma = soma + numero
    quantidade_de_numeros = quantidade_de_numeros +1

