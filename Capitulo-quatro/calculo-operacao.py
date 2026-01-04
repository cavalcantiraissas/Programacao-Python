primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
operacao = str(input("Qual operação você deseja realizar?\n - Soma\n - Subtração\n - Multiplicação\n - Divisão\n"))

if operacao == 'Soma':
    resultado = primeiro_numero + segundo_numero
    print(resultado)

elif operacao == 'Subtração': 
    resultado = primeiro_numero - segundo_numero
    print(resultado)

elif operacao == 'Multiplicação': 
   resultado = primeiro_numero * segundo_numero
   print(resultado)

else:
    resultado = primeiro_numero / segundo_numero
    print(resultado)
