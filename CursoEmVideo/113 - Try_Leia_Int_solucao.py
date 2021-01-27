def leiaInt(msg):
	while True:
		try:
			nr = int(input(msg))
		except(ValueError, TypeError):
			print('Por favor digite um número inteiro válido')
			continue
		except(KeyboardInterrupt):
			print('O utilizador preferiu não digitar esse número')
			return 0
		else:
			return nr

def leiaFloat(msg):
	while True:
		try:
			nr = float(input(msg))
		except(ValueError, TypeError):
			print('Por favor digite um número real válido')
			continue
		except(KeyboardInterrupt):
			print('O utilizador preferiu não digitar esse número')
			return 0
		else:
			return nr

a = leiaInt('Digite um valor: ')
b = leiaFloat('Digite outro valor: ')
print(f'O valor inteiro digitado foi {a} e o real foi {b}')