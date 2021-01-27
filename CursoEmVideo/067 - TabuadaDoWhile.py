
while True:
	tabuada = int(input("Digite um nr para ver a sua tabuada: "))
	style = "-"
	if tabuada < 0:
		break
	print(f"{style*20}")
	for i in range(1,11):
		print(f"{tabuada} x {i:^4} = {tabuada*i}")
	print(f"{style*20}\n")
print(f"Programa terminado, nao sao aceitaveis numeros negativos, tais como {tabuada}")
