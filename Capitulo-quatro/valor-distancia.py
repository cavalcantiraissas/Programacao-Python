distancia_percorrida = float(input("Quantos KM você deseja percorrer?\n"))

if distancia_percorrida <= 200:
    valor_km = 0.50
    valor_total = distancia_percorrida * valor_km
    print(f"Você deverá pagar R$ {valor_total}\n")
else:
    valor_km = 0.45
    valor_total = distancia_percorrida * valor_km
    print(f"Você deverá pagar R$ {valor_total}\n")
