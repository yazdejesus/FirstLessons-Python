from datetime import date as ano

ano_nasc = int(input('Olá, qual o seu ano de nascimento?'))

idade = 2020 - ano_nasc
# idade = ano.today().year - ano_nasc

if idade <= 14:
	if idade <= 9:
		print(f'Idade: {idade} anos.\n Classificação: MIRIM')
	else:
		print(f'Idade: {idade} anos.\n Classificação: INFANTIL')
elif idade <= 19:
	print(f'Idade: {idade} anos.\n Classificação: JUNIOR')
elif idade > 25:
	print(f'Idade: {idade} anos.\n Classificação: MASTER')
else:
	print(f'Idade: {idade} anos.\n Classificação: SENIOR')
