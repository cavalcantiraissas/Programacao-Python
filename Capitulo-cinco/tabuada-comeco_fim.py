numero = int(input("Tabuada de: "))
inicio_tabuada = int(input("Começando em qual número? "))
fim_tabuada = int(input("Terminando em qual número? "))

while inicio_tabuada<=fim_tabuada:
    print(f"{numero} X {inicio_tabuada} = {numero *inicio_tabuada}")
    inicio_tabuada = inicio_tabuada+1
