from time import sleep
from random import sample

print(f"{'-'*35}\n{'TOTOLOTO':^35}\n{'-'*35}")
opcoes = int(input("Quantos jogos pretendes sortear? "))
print(f"{' SORTEANDO JOGOS ':=^35}")

for c in range (0,opcoes):
    sleep(1)
    print(f"Jogo {c+1}: ", end="")
    sorteio = sample(range(1,60),6)
    print(sorteio)
print(f"{' < OBRIGADO! > ':=^35}")