temp = list()
pessoas = list()
tempmax = list()
tempmin = list()

while True:
    nome = input("Digite o nome da pessoa (ou 0 para sair): ").title()
    if nome == '0':
        break
    peso = float(input(f"Digite o peso do {nome}: "))
    temp.append(nome)
    temp.append(peso)
    pessoas.append(temp[:])
    temp.clear()
    print(f"{nome} foi adicionado ao cadastro, com o peso {peso}\n")

print(f"Ao todo foram cadastradas {len(pessoas)} pessoas")

for c, val in enumerate(pessoas):
    if c == 0:
        maxval = minval = val[1]
    else:
        if maxval < val[1]:
            maxval = val[1]
        elif minval > val[1]:
            minval = val[1]

#A solução proposta inclui esta iteração no while acima. Diminui 1 for

for val in pessoas:
    if maxval == val[1]:
        tempmax.append(val[0])
    if minval == val[1]:
        tempmin.append(val[0])

#A solução proposta evita as listas temp e ja imprime os valores max e min directo

print(f"O maior peso foi de {maxval} kg. Peso de {tempmax}")
print(f"O menor peso foi de {minval} kg. Peso de {tempmin}")