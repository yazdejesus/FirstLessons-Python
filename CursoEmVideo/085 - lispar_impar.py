lista_par = list()
lista_impar = list()
lista = [lista_par,lista_impar]

for c in range(0,7):
	x = int(input(f"Digite o {c+1}o numero: "))
	if x % 2 == 0:
		lista_par.append(x)
	else:
		lista_impar.append(x)

print(f"Os numeros pares digitados foram: {sorted(lista_par)}")
print(f"Os numeros impares digitados foram: {sorted(lista_impar)}")