import moeda

tako = float(input('Digite o preço: MZN_'))
print(f'A metade de {moeda.moeda(tako)} é {moeda.moeda(moeda.metade(tako))}')
print(f'O dobro de {moeda.moeda(tako)} é {moeda.moeda(moeda.dobro(tako))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(tako, 10))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(tako, 13))}')