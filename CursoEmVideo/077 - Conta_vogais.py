palavras = (input("Introduza uma palavra: ").lower(),input("Introduza mais uma palavra: ").lower(),
input("e mais uma: ").lower(),input("Ok, a penultima: ").lower(),
input("Introduza a ultima palavra: ").lower(),input("Introduza a palavra bonus: ").lower())

print(f"As palavras digitadas foram {palavras}")

vogais = 0
for palavra in palavras:
	count = 0
	vogal = []
	for letra in palavra:
		if letra in 'aeiou':
			vogal.append(letra)
			count +=1
			vogais+=1
	print(f"A palavra {palavra.upper} tem {count} vogais: {vogal}")
print(f"Ao todo foram {vogais} vogais")