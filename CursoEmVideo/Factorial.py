numero = int(input("Introduza um nr para ver o seu factorial: "))
factorial = numero
i = numero-1

while i > 0:
	factorial *= i
	i -= 1
	#print (factorial)
print(f"\nO factorial do numero {numero} é {factorial}")
	