lista = [list(),list()]
print(lista)

for c in range(0,7):
    x = int(input("Digite o {c+1}o numero: "))
    if x % 2 == 0:
        lista[0].append(x) #magic trick
    else:
        lista[1].append(x)

print(f"Os numeros pares digitados foram: {sorted(lista[0])}")
print(f"Os numeros impares digitados foram: {sorted(lista[1])}")

#nota importante: como visto acima, é possível adicionar à lista da lista referenciando a sua posição