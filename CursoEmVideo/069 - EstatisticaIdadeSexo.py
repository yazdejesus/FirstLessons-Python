#ler idade de varias pessoas e perguntar se quer continuar ou nao
#mostrar total de maiores de 18 anos; total de homens; total de mulheres < 20

maiores_de_idade = homens = mulheres_menores = 0
ronda = 0

while True:
	ronda += 1
	idade = int(input(f"\nIntroduza a idade da {ronda}a pessoa: "))
	sexo = input("Introduza também o seu sexo (m/f): ").upper()
	continuar = input("\nDeseja continuar (y/n)? ").upper()
		
	if idade > 18:
		maiores_de_idade += 1
	if sexo == "M":
		homens += 1
	if sexo == "F": #tambem possivel concatenar os ifs com 'and'
		if idade < 20:
			mulheres_menores += 1

	if continuar == "N":
		break

print(f"\nPrograma encerrado.\nVoce registrou {ronda} pessoas, das quais:\n{maiores_de_idade} sao maiores de 18 anos,\n{homens} sao homens e\n{mulheres_menores} sao mulheres abaixo de 20 anos")
