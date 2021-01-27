#Aprimorar o exercicio abaixo para que possa receber mais jogadores até o user parar (S/N)
#No final mostrar a lista de jogadores numa tabela, incl distribuicao dos golos e total
#O programa também deve permitir ver o detalhe de cada jogador (distribuicao |)
#E validar inputs

jogador = dict()
clube = list()

while True:
    jogador["nome"] = input("Nome do jogador: ").title()
    lista_golos = []
    jogador["golos"] = []
    nr_jogos = int(input(f"Quantos jogos o {jogador['nome']} fez? "))
    for i in range (1,(nr_jogos + 1)):
        lista_golos.append(int(input(f"   -Golos marcados no {i}o jogo: ")))
    jogador["golos"] = lista_golos[:]
    jogador["total"] = sum(lista_golos)
    clube.append(jogador.copy())
    lista_golos.clear()
    while True:
        stop = input("Deseja continuar? (S/N) ").upper()
        if stop in "SN":
            break
        print("Digite apenas S ou N")
    if stop == "N":
        break
    print()
print('-='*31)
print("cod\tnome\t\tjogos\tgolos\t\t\ttotal")
print('-'*60)
for pos,player in enumerate(clube):
    print(f"{pos}\t{player['nome']:<15}{len(player):^5}\t{str(player['golos']):<20}{player['total']:>8}")
print('-'*60)

while True:
    detalhe = int(input("Digite o codigo do jogador para ver detalhes (999 parar): "))
    if detalhe >= len(clube):
        if detalhe == 999:
            break
        print(f"Nao existe jogador {detalhe}.")
        detalhe = int(input("Digite um codigo valido para detalhes (999 parar): "))
    print(f"\t*** LEVANTAMENTO DO JOGADOR {clube[detalhe]['nome']}:")
    for pos,jogo in enumerate(clube[detalhe]["golos"]):
        print(f"\t- No {pos+1}o jogo fez {jogo} golos")
    print('-'*60)
print("\nJogo encerrado, volte sempre!")
print('-='*27,'FIM!!!')
