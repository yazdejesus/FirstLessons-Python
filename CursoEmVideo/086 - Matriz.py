matriz = [[0,0,0],[0,0,0],[0,0,0]]
#print(matriz)
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um numero na posicao {[linha]}{[coluna]}: "))
print("-="*30)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"|{matriz[linha][coluna]:^5}|",end="")
    print()
print("-="*30)

soma_par = 0
for linha in range(0,3): # a solucao proposta é incluir o if deste ciclo
    for coluna in range(0,3): # no ciclo anterior
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
print(f"A soma dos valores pares é {soma_par}")

soma_col3 = 0
for linha in range(0,3):
    soma_col3 += matriz[linha][coluna] # ou matriz[linha][2]
print(f"A soma dos valores da 3a coluna é {soma_col3}")
print(f"O maior valor da 2a linha é {max(matriz[1])}")