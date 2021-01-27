def factorial(num, show=False):
	"""
	=> Calcula o factorial de um número.
	:param num: o número  ser calculado.
	:param show: (opcional) Mostra ou não a conta.
	:return: o valor do factorial do número 'num'.
	"""
	factorial_ = 1
	print('-'*40)
	for n in range(num, 0, -1):
		if show == True:
			if n != 1:
				print(f'{n} x', end=' ')
			else:
				print(f'{n} =', end=' ')
		factorial_ *= n
	return factorial_

factor = int(input('Digite um nr para ver o seu factorial '))
mostrar = input('Deseja ver os detalhes? Sim/Nao ')[0].upper()
if mostrar == 'S':
	mostrar = True
else:
	mostrar = False
print(factorial(factor,mostrar))