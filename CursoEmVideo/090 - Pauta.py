pauta = {}
pauta['nome'] = input("Nome: ")
pauta['media'] = float(input("Media: "))
print('-='*20)
if pauta['media'] >= 14:
    pauta['situacao'] = 'Aprovado'
elif pauta['media'] < 8:
    pauta['situacao'] = 'Reprovado'
else:
    pauta['situacao'] = 'Recuperacao'

for k,v in pauta.items():
    print(f" - {k} é igual a {v}")