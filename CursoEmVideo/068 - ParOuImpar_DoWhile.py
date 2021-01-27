#jogar par ou ímpar com o computador
#só termina quando perder
#calcula total de rondas e vitorias

from random import randint

resultado = "Ganhou"
rondas = vitorias = 0

while True:
	computador = randint(1,10)
	par_impar = input("Escolha Par ou Impar (P/I): ").upper()
	jogador = int(input("Que numero vais jogar? "))
	soma = jogador + computador
	rondas += 1

	if par_impar not in "PI":
		par_impar = input("Escolha ou P para Par ou I para Impar (P/I): ").upper()

	if par_impar == "P":
		if soma % 2 == 0:
			resultado = "Ganhou"
		else:
			resultado = "Perdeu"
	elif par_impar == "I":
		if soma % 2 != 0:
			resultado = "Ganhou"
		else:
			resultado = "Perdeu"
			
	if resultado == "Ganhou":
		print(f"Parabens, voce ganhou. Computador escolheu {computador} e voce escolheu {jogador}.\n")
		vitorias += 1
	elif resultado == "Perdeu":
		print(f"Ups, voce perdeu. Computador escolheu {computador} e voce escolheu {jogador}.\n")
		break
print(f"Jogo terminado. Obrigado por jogar connosco.\n      Ao fim de {rondas} rondas voce ganhou {vitorias}")
