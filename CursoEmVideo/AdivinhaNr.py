from random import randint
from time import sleep

computador = randint(0,10)
ask = int(input("Adivinhe o nr que o computador pensou: "))
tentativas = 1

while ask != computador:
	ask = int(input("Errou!!!\nAdivinhe o nr que o computador pensou: "))
	tentativas += 1

print (f"Parabéns, teu palpite foi {ask} e o computador também pensou {computador}.\n Foram necessarias {tentativas} tentativas!")

#Dica: inicializar acertou como False e usar while not acertou para verificar a condição.
#Dica: Outra dica é acrescentar frio/quente para torná-lo mais divertido