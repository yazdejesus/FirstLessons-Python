import moeda

tako = float(input('Digite o preço: MZN_'))
print(f'A metade de {tako}MZN é {moeda.metade(tako)}MZN')
print(f'O dobro de {tako}MZN é {moeda.dobro(tako)}MZN')
print(f'Aumentando 10%, temos {moeda.aumentar(tako, 10)}MZN')
print(f'Diminuindo 13%, temos {moeda.diminuir(tako, 13)}MZN')