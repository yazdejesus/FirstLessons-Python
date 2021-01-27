sexo = input("Introduza o sexo: ")
while sexo not in "MmFf":
	sexo = input("A sério? Digite apenas M ou F")
print(f"Parabéns, o teu sexo é {sexo}")