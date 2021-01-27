#ler varios nr inteiros, até digitarem 999
#mostrar a soma e a quantidade dos nrs digitados

soma = contagem = 0
maior = menor = 0
while True:
	numero = int(input("Digite um nr (ou 999 para sair): "))
	if numero == 999:
		break
	if contagem == 0:
		menor = numero
	if numero > maior:
		maior = numero
	if numero < menor:
		menor = numero
	soma += numero
	contagem +=1
print(f"Digitaste {contagem} numeros, cuja soma é {soma}.\nO maior foi {maior} e o menor foi {menor}")
