primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
quociente = 0

while primeiro_numero >=segundo_numero:
    primeiro_numero = primeiro_numero - segundo_numero
    quociente = quociente + 1
   
print(f"Resto da Divisão: {primeiro_numero}")
print(f"Quociente: {quociente}")
