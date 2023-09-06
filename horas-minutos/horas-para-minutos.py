horas = input('Insira horas: ')
minutos = input('Insira os minutos: ')

horas = int(horas)
minutos = float(minutos)

minutos_decimal = minutos / 60
minutos_formatados = "{:.2f}".format(minutos_decimal) # Formatando os numeros com duas casas decimais

# Verifique se os minutos são menores que 10 e, se sim, remova o zero à esquerda
if minutos_decimal < 10:
    minutos_formatados = minutos_formatados[1:]

print(f'Sua hora em minutos decimais é {horas}{minutos_formatados}')
