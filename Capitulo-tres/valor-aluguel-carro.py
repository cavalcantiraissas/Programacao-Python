dias_uso = float(input("Por quantos dias o veículo foi alugado?\n"))
km_uso = float(input("Quantos Km's foram pecorridos?\n"))

km_pecorrido  = 0.15 * km_uso
quantidade_dias = 60 * dias_uso
valor_total = km_pecorrido + quantidade_dias

print(f"Valor total: R$ {valor_total}\n")
