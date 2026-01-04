primeiro_numero = int(input("Digite o primeiro número:\n")) #A
segundo_numero = int(input("Digite o segundo número:\n")) #B
terceiro_numero = int(input("Digite o terceiro número:\n")) #C

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero: # A é maior
  if segundo_numero > terceiro_numero:
     print(f"{primeiro_numero} é o maior e {terceiro_numero} é o menor")
  else:
     print(f"{primeiro_numero} é o maior e {segundo_numero} é o menor")

elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero: # B é maior
    if primeiro_numero > terceiro_numero:
     print(f"{segundo_numero} é o maior e {terceiro_numero} é o menor")
    else:
     print(f"{segundo_numero} é o maior e {primeiro_numero} é o menor")

elif terceiro_numero > primeiro_numero and terceiro_numero > segundo_numero: # C é maior
    if segundo_numero > primeiro_numero:
       print(f"{terceiro_numero} é o maior e {primeiro_numero} é o menor")
    else:
       print(f"{terceiro_numero} é o maior e {segundo_numero} é o menor")
else:
    print("Todos os números são iguais.")
