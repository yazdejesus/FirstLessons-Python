velocidade = float(input('Qual a velocidade do seu carro? Km/h _'))
if velocidade > 80:
	excesso = velocidade - 80
	print(f'Você excedeu em {excesso:.2f} Km/h o limite de velocidade e a sua multa é de {excesso*7:.2f} MZN')
print('Continuação de boa viagem')
