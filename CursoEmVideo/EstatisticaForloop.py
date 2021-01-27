#ler nome idade e sexo de 4 pessoas
#calcular media de idade, nome do mais velho, nr de idades < que 20
max_idade = nr_meninas = soma = media = 0
nome_kota = ""
for i in range (1,5):
    nome = input("Digite o seu nome: ").title()
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo (M/F)").upper()
    soma += idade
    media = soma/i
    if idade > max_idade:
        nome_kota = nome
        max_idade = idade
    if sexo == 'F':
        if idade < 20:
            nr_meninas += 1
print(f"A pessoa mais velha chama-se {nome_kota} e tem {max_idade} anos.")
print(f"A media de idade é {media}")
print(f"Existem {nr_meninas} mulheres abaixo de 20 anos")