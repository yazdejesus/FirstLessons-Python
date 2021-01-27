from time import sleep

def contador(inicio, fim, intervalo):
	if intervalo < 0:
		intervalo *= -1
	if intervalo == 0:
		intervalo = 1
	
	print('-='*25)
	print(f'Contagem de {inicio} até {fim} de {intervalo} em {intervalo}')
	conta = inicio
		
	if inicio < fim:
		while conta <= fim:
			print(conta, end=' ', flush=True)
			conta += intervalo
			sleep(0.5)
	elif fim < inicio:
		while conta >= fim:
			print(conta, end=' ', flush=True)
			conta -= intervalo
			sleep(0.5)
	print('FIM!')
	sleep(1)
	print('-='*25)

contador(1,10,1)
contador(10,0,2)

print('Agora é sua vez de personalizar a contagem!')
comecar = int(input('Inicio: '))
terminar = int(input('Fim: '))
salto = int(input('Passo: '))
contador(comecar, terminar, salto)
