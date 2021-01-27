from random import randint

numeros = []

def sorteia_num():
	print('Sorteiando 5 numeros: ')
	for i in range(5):
		numeros.append(randint(0,20))
		print(numeros[i], end=' ')
	print()
	print(sorted(numeros))
	return numeros

def soma_par(lista):
	soma = 0
	for num in lista:
		if num % 2 == 0:
			soma += num
	print(f'A soma dos valores pares da lista {lista} é {soma}')

sorteia_num()
soma_par(numeros)