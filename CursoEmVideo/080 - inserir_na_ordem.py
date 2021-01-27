lista = list()

for n in range(0,5):
	x = int(input("Digite um numero: "))
	if len(lista) == 0:
		lista.append(x)
	else:
		if x <= min(lista):
			pos = lista.index(min(lista))
			lista.insert(pos, x)
		elif x >= max(lista):
			pos = lista.index(max(lista))
			lista.insert(pos+1, x)

# alternativamente, pode ser usado um while:
#   if n == 0 or x>lista[-1]:
#       lista.append(x)
#   else:
#       pos = 0
#       while pos < len(lista):
#           if x <= lista[pos]:
#               lista.insert(pos, x)
#               break
#           pos += 1
#
print(lista)