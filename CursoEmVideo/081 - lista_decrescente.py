lista = list()
cont = 0

while True:
	cont += 1
	lista.append(int(input("Introduza um nr: ")))
	continuar = input("Deseja continuar? (S/N) _").strip().upper()[0]
	if continuar == "N":
		break

print(f"Foram digitados {cont} numeros")
#ao inves de ter uma variavel, pode ser mais eficiente usar apenas o length

print(sorted(lista, reverse=True))

if 5 in lista:
	print(f"O numero 5 consta da lista na posicao {lista.index(5)}")
else:
	print("O numero 5 nao consta da lista")