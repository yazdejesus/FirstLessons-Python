def leia_Int(num):
	while True:
		nr = input(num)
		if nr.isdigit():
			return nr
			#break; #no need to break as the function exits once it finds a return statement
		else:
			#print('\033[1;31nERRO! Digite um número inteiro válido.\033[n') #colors not working in cmd
			print('ERRO! Digite um número inteiro válido.')



n = leia_Int('Digite um número: ')
print(f'Voce acabou de digitar o número {n}')