#ler nome e preço de vários produtos. Perguntar se vai continuar
#total gasto na compra, nr de produtos acimia de 1000 e nome do mais barato

total = bem_caros = 0
compra = mais_barato = 0

while True:
	nome = input("Introduza o nome do produto: ")
	preco = float(input("Introduza o preco do produto: MZN_"))
	continuar = input("\nDeseja continuar (y/n)? ").upper()
	
	total += 1
	compra += preco
	
	if preco > 1000:
		bem_caros += 1
	
	if total == 1:
		mais_barato = preco
		nome_mais_barato = nome
		print(nome_mais_barato, mais_barato)
	else:
		if mais_barato > preco:
			mais_barato = preco
			nome_mais_barato = nome
			print(nome_mais_barato,mais_barato)
	
	if continuar == "N":
		break

print(f"\n\nCompra encerrada, vide o recibo:\nTotal de itens: {total}\nCusto Total: {compra:.2f}\nProdutos acima de 1000 MZN: {bem_caros}\nProduto mais barato: {nome_mais_barato} (custo {mais_barato})")
