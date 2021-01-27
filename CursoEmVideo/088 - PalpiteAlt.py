from random import randint
from time import sleep

print(f"{'-'*35}\n{'TOTOLOTO':^35}\n{'-'*35}")
opcoes = int(input("Quantos jogos pretendes sortear? "))
print(f"{' SORTEANDO JOGOS ':=^35}")

palpite = []
for a in range(0,opcoes):
    for c in range(0,6):
        while True:
            num = randint(1,60)
            if num in palpite:
                num = randint(1,60)
            else:
                break
        palpite.append(num)
    print(f"Jogo {a+1}: {palpite}")
    palpite.clear()
    sleep(1)
    
print(f"{' < OBRIGADO! > ':=^35}")
#A solucao proposta usa 2 whiles, muitos contadores e... mais importante...
# uma lista maior para receber cada "palpite"