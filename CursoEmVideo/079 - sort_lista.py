lista = list()
limite = int(input("Quantos nrs queres digitar? "))
for c in range(0,limite):
    x = int(input("Digite um nr: "))

    if x not in lista:
        lista.append(x)
    else:
        print(f"O valor {x} já existe na lista")

print(lista)
print(sorted(lista))