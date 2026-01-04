salario_atual = float(input("Quanto você recebe atualmente?\n"))

if salario_atual > 1250:
    novo_salario = salario_atual + (salario_atual * 10 / 100)
    print(f"Você passará a receber: R$ {novo_salario}")
else:
    novo_salario = salario_atual + (salario_atual * 15 / 100)
    print(f"Você passará a receber: R$ {novo_salario}")
