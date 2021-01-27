import moeda

tako = float(input('Digite o preço: MZN_'))
print(f'A metade de {moeda.moeda(tako)} é {moeda.metade(tako, True)}')
print(f'O dobro de {moeda.moeda(tako)} é {moeda.dobro(tako, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(tako, 10, True)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(tako, 13, True)}')