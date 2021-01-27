termo = int(input("Introduza o primeiro termo da PA: "))
razao = int(input("Introduza a razao da PA: "))
soma = i = 0
limite = 10
round = 1

while limite != 0:
    soma += limite
    while i <limite:
        termo += razao
        print(termo, end=" | ")
        i += 1
    limite = int(input("\nQuantos mais termos deseja exibir: "))
    i = 0
    round += 1
print(f"\nVoce escolheu terminar após {round} interacoes e {soma} termos exibidos.")