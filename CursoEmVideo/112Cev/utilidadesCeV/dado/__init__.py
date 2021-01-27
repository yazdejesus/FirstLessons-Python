def leia_dinheiro(valor):
	while True:
		val = input(valor).replace(',','.').strip()
		if val.isalpha() or val == '':
			print(f'ERRO: "{val}" é um preço inválido!')
		else:
			preco = float(val)
			return preco