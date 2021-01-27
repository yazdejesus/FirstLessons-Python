from time import sleep
#fazer um mini-sistema que use o help(arg)
#user digita o comando
#o manual aparece na tela
#termina ao digitar FIM
def mini_help(n):
	"""
	=> Exibe a docstring do comando que recebe
	:param n: o comando a ser pesquisado
	:return: a ajuda interactiva (help) do parametro
	"""
	r = len('Acedendo ao manual do comando')+len(n)+6 #este trecho
	print('~'*r)									#de codigo
	print(f'  Acedendo ao manual do comando {n}')	#pode ser
	print('~'*r)									#sub por uma def
	return help(n)


while True:
	print('~'*28)
	print(f'  SISTEMA DE AJUDA PyHELP')
	print('~'*28)
	sleep(0.5)
	texto = input('Digite a função ou Biblioteca :> ').lower()
	sleep(0.5)
	if texto == 'fim':
		break
	else:
		mini_help(texto)