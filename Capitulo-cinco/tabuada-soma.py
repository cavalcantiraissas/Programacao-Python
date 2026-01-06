primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))
resultado_sucessivo = 0
contador = 0 

while contador < segundo_numero:
    resultado_sucessivo = resultado_sucessivo + primeiro_numero
    contador = contador + 1 
print(f"{primeiro_numero} X {segundo_numero} = {resultado_sucessivo}")
