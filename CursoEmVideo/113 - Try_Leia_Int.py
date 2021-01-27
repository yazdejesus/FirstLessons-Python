def leia_Int(msg):
	while True:
		nr = input(msg)
		if nr.isdigit():
			return nr
		else:
			print('ERRO! Digite um número inteiro válido.')

def leia_Float(msg):
	while True:
		nr = input(msg).replace(',','.')
		if nr.isalpha() or nr.isdigit() or nr.strip() == '':
			print('ERRO! Digite um número real válido.')
		else:
			return nr


try:
	a = leia_Int('Digite um número inteiro: ')
	b = leia_Float('Digite um número Real: ')
except KeyboardInterrupt:
	print('\nO usuario preferiu não digitar esse número')
	b = 0
	try:
		print(a)
	except NameError:
		a = 0
finally:
	print(f'O valor inteiro digitado foi {a} e o real foi {b}')