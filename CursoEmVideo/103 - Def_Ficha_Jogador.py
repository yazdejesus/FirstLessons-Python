def ficha_player(nome='<desconhecido>',golos=0):
	print('-'*40)
	if golos == 1:
		print(f'O jogador {nome} fez {golos} golo no campeonato')
	else:
		print(f'O jogador {nome} fez {golos} golos no campeonato')


nome_jogador = input('Nome do jogador: ')
num_golos = input('Número de golos: ')

if num_golos.isdigit() == True:
	num_golos = int(num_golos)
else:
	num_golos = 0

if nome_jogador.strip() == '':
	ficha_player(golos=num_golos)
else:
	ficha_player(nome_jogador,num_golos)