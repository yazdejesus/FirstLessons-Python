def metade(num=0):
	return num/2

def dobro(num=0):
	return num*2

def aumentar(num=0, perc=0):
	perc /= 100
	return num + num*perc

def diminuir(num=0, perc=0):
	perc /= 100
	return num - num*perc

def moeda(preco = 0, moeda = 'MZN_'):
	return f'{moeda}{preco:.2f}'.replace('.',',')