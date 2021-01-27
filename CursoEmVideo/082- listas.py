lista = list()
lista_par = list()
lista_impar = list()

while True:
	lista.append(int(input("Introduza um nr: ")))
	continuar = input("Deseja continuar? (S/N) _").strip().upper()[0]
	if continuar == "N":
		break

for c in lista:
    if c % 2 == 0:
        lista_par.append(c)
    else:
        lista_impar.append(c)

print(f"A lista completa é:   {lista}")
print(f"A lista de pares é:   {lista_par}")
print(f"A lista de ímpares é: {lista_impar}")