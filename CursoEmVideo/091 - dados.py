from random import randint
from time import sleep

dados = dict()
for i in range(1,5):
    nome = 'jogador' + str(i)
    dados[str(nome)] = randint(1,6)
    i += 1
print('-='*20,'\nRolem os dados:')

for k,v in dados.items():
    sleep(1)
    print(f"O {k} tirou {v} no dado.")
print('-='*20,'\n')

print(f"{'=*'*20}\n{' RANKING DOS JOGADORES ':^40}\n{'=*'*20}")

#print(key, value) for (key, value) in sorted(dados.items(), key=lambda x : x[1], reverse=True)

reversed_dados = sorted(dados.items(), key=lambda x : x[1], reverse=True)

#ao invés de usar o lambda, pode-se usar um módulo chamado itemgetter, que faz parte do operator
#então seria apenas from operator import itemgetter e aí usar o itemgetter no key

c = 1
for x in reversed_dados:
    sleep(1)
    print(f"Em {c}o lugar: {x[0]} que tirou {x[1]}")
    c += 1

#ao inves de usar a variável pode-se 'enumerate' a lista organizada

print('-='*13,'Fim, Obrigado!')