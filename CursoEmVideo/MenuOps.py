nr1 = float(input("Digite um numero para operador esquerdo: "))
nr2 = float(input("Digite um numero para operador direito: "))
menu = resultado = 0
#menu = int(input("\n*****MENU*****\nDigite uma das opcoes abaixo\n[1] somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n   "))

while menu != 5:
	menu = int(input("\n*****MENU*****\nDigite uma das opcoes abaixo\n[1] somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n   "))
	if menu == 1:
		resultado = nr1 + nr2
		print(f"A soma dos operandos é {resultado:.2f}")
#		menu = int(input("\n*****MENU*****\nDigite uma das opcoes abaixo\n[1] somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n   "))
	elif menu == 2:
		resultado = nr1 * nr2
		print(f"O resultado da multiplicacao é {resultado:.2f}")
#		menu = int(input("\n*****MENU*****\nDigite uma das opcoes abaixo\n[1] somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n   "))
	elif menu == 3:
		resultado = max(nr1,nr2)
		print(f"O nr {resultado} é o maior dentre os 2")
#		menu = int(input("\n*****MENU*****\nDigite uma das opcoes abaixo\n[1] somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n   "))
	elif menu == 4:
		nr1 = float(input("Digite um numero para operador esquerdo: "))
		nr2 = float(input("Digite um numero para operador direito: "))
#		menu = int(input("\n*****MENU*****\nDigite uma das opcoes abaixo\n[1] somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n   "))
	else:
		pass
#		menu = int(input("\n*****MENU*****\nDigite um valor valido dentre as opcoes abaixo\n[1] somar\n[2]multiplicar\n[3]maior\n[4]novos numeros\n[5]sair do programa\n   "))
print("Voce escolheu sair, obrigado!")