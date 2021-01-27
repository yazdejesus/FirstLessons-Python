jogador = dict()

jogador["nome"] = input("Nome do Jogador: ").title()
jogador["jogos"] = []
nr_jogos = int(input("Nr de jogos na temporada: "))
total = 0
for i in range(1, (nr_jogos+1)):
    golos = int(input(f"\tNr de golos no {i}o jogo: "))
    jogador["jogos"].append(golos)
    total += golos #alternativa seria criar uma lista, fazer o append via for
jogador["total"] = total #como feito aqui, e depois lançar a copia da lista no dicionario
#                         aí o total era fazer apenas sum(lista)
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-='*30)
print(f"O jogador {jogador['nome']} fez {len(jogador['jogos'])} jogos:")
for e,i in enumerate(jogador["jogos"]):
    print(f"\t=>No jogo {e+1} fez {i} golos")
print(f"Foi um total de {jogador['total']} golos")
