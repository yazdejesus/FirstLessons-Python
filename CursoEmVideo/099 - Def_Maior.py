def calMaior(*args):
	maior = 0
	for num in args:
		if num > maior:
			maior = num
	print('-='*30)
	print('Analisando os valores passados...')
	print(f'{args} foram informados {len(args)} valores no total.')
	print(f'O maior valor informado foi {maior}')

calMaior(2,9,5,8,3,5)
calMaior(1,5)
calMaior(5,1)
calMaior()