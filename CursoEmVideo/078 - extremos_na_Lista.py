lista = list()

for r in range(0,5):
	lista.append(int(input("Introduza um numero: ")))

print(f"O maior valor foi {max(lista)}, que se encontra na {lista.index(max(lista))+1}a posicao\ne o menor valor foi {min(lista)}, que se encontra na {lista.index(min(lista))+1}a posicao")
