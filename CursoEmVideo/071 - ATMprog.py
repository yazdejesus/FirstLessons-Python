#simular o funcionamento de uma ATM
##perguntar quanto quer levantar
##e dizer quantas notas de 50,20,10,1 vao sair

x = "*"
label = "BANCO Y"
print(f"{x*50:^50}\n{label:^50}\n{x*50:^50}\n")

saque = int(input("Bem vindo, quanto pretende levantar? MZN_"))
saldo = saque

while True:
    saldo = saldo // 
    if 

'''
Primeira versao do codigo, sem repeticao
notas_50 = saque // 50
resto_50 = saque - notas_50*50
notas_20 = resto_50//20
resto_20 = resto_50 - notas_20*20
notas_10 = resto_20//10
resto_10 = resto_20 - notas_10*10
notas_1 = resto_10
'''

print(f"O teu levantamento de {saque} está dividido em\n{notas_50} notas de 50\n{notas_20} notas de 20\n{notas_10} notas de 10\n{notas_1} notas de 1")
