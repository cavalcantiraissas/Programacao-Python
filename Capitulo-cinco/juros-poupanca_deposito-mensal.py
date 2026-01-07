valor_inicial = float(input("Valor do depósito inicial: "))
deposito_mensal = float(input("Valor do depósito mensal: "))
taxa_juros = float(input("Taxa de juros mensal (%): "))

saldo = valor_inicial
total_depositado = valor_inicial

for mes in range(1, 25):
    saldo += deposito_mensal
    total_depositado += deposito_mensal

    saldo += saldo * (taxa_juros / 100)

    print(f"Mês {mes}: Saldo = R$ {saldo:.2f}")

lucro = saldo - total_depositado

print(f"\nTotal depositado: R$ {total_depositado:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")
print(f"Lucro: R$ {lucro:.2f}")
