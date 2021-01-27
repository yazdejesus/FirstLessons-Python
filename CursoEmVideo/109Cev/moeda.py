def metade(num=0, formatar=False):
	res = num/2
	if formatar == True:
		return moeda(res)
	else:
		return res

def dobro(num=0, formatar=False):
	res = num*2
	return moeda(res) if formatar is True else res

def aumentar(num=0, perc=0, formatar=False):
	res = num + num*(perc/100)
	return res if formatar is False else moeda(res)

def diminuir(num=0, perc=0, formatar=False):
	res = num - num*(perc/100)
	return res if not formatar else moeda(res)

def moeda(preco = 0, moeda = 'MZN_'):
	return f'{moeda}{preco:.2f}'.replace('.',',')