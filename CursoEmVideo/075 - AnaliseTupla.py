a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite mais um numero: "))
d = int(input("Digite o último numero: "))

numeros = (a, b, c, d)

#Ao inves de criar varias temporarias, a forma mais eficiente, em termos de memoria
#seria colocar todos os inputs dentro da tupla, da seguinte forma
#numeros = (int(input("digite nr")),int(input("digite nr")),
#           int(input("digite nr")),int(input("digite nr")))
#Assim teríamos a tupla criada de boa e sem gastar memória com variáveis

print(f"Voce digitou os valores {numeros}")
print(f"O valor 9 apareceu {numeros.count(9)} vezes")

if 3 in numeros:
    print(f"O valor 3 apareceu pela primeira vez na {numeros.index(3)+1}a posicao")
else:
    print("Nao foi digitado o numero 3")

count = 0
for n in numeros:
    if n != 0 and n % 2 == 0:
        count += 1
print(f"Foram digitados {count} numeros pares")