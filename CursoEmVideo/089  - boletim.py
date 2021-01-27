pauta = []
templis = []
contador = 0
while True:
    pauta.append(templis[:])
    nome = input("Nome: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    stop = input("Quer continuar? (s/n)").upper()

    pauta[contador].append(nome)
    pauta[contador].append(nota1)
    pauta[contador].append(nota2)
    templis.clear()
    contador += 1
#A solucao mais simples é ler tudo e fazer o append ja como lista.    
    if stop == "N": #Sem necessidade de contadores ou
        break #de listas temporarias

print('-='*15)

print(f"{'No.':<5}{'NOME':<15}{'MEDIA':>10}\n{'-'*30}")
for p in range(0,len(pauta)):
    media = (pauta[p][1] + pauta[p][2])/2
    print(f"{p:<5}{pauta[p][0]:<15}{media:>10}")
print('-'*30)

while True:
    var = int(input("Digite o codigo do aluno para ver as notas (999 para sair): "))
    if var == 999:
        break
    print(f"As notas do {pauta[var][0]} são: [{pauta[var][1]}, {pauta[var][2]}]\n")

print(f"{'-='*3}{' FIM DO PROGRAMA '}{'=-'*3}")