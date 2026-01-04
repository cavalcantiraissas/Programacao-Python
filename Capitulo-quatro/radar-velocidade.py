velocidade_carro = float(input("Digite a velocidade do carro:\n"))

if velocidade_carro > 80:
    multa = (velocidade_carro -80) * 5
    print(f"Você deverá pagar: R$ {multa:.2f} por excesso de velocidade.")
else:
    print("Você está dentro do limite permitido.")
