dias, horas, minutos, segundos = map(int, input("Digite a quantidade de dia, horas, minutos e segundos, respectivamente:\n").split())

conversao_dias = (dias * 86400)
conversao_horas = (horas * 3600)
conversao_minutos = (minutos * 60)

total_segundos = conversao_dias + conversao_horas + conversao_minutos + segundos
print(total_segundos)
