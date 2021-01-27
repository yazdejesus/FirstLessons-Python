from random import randint as r

star = '*'
tentativas = 1
result = 0
nome = input(f"{star*5}Bem vindo ao jogo de adivinhas{star*5}\n Com quem temos o prazer de jogar?\n")
minimo = int(input(f"Obrigado {nome}. Introduza o valor mínimo a adivinhar\n"))
maximo = int(input("Introduza o valor máximo a adivinhar\n"))

while result != 1:
  check = maximo - minimo
  if	check < 0:
    maximo = int(input(f"Ah não {nome}, o valor máximo deve ser superior ao valor mínimo.\n Introduza novamente o valor máximo a adivinhar\n"))
  elif check == 0:
    maximo = int(input(f"Espertinho neh {nome}, mas aqui não vale. O valor máximo deve ser superior ao valor mínimo, não igual.\n Introduza novamente o valor máximo a adivinhar\n"))
  elif check < 5:
    maximo = int(input(f"Assim não terá graça {nome}. O intervalo é muito curto.\n Introduza novamente o valor máximo a adivinhar\n"))
  else:
    result = 1

rondas = int(input(f"Muito bem {nome}, agora introduza o número máximo de tentativas para adivinhar\n"))+1
computer = r(minimo,maximo)
player = int(input(f"{tentativas}a tentativa: Adivinhe o valor no intervalo de {minimo} a {maximo}\n"))
for tentativas in range(1,rondas):
    tentativas += 1
    if player == computer:
        msg = input(f"\n Parabéns, você escolheu {player} e acertou, pois nós também haviamos escolhido {computer}.\n Nr de tentativas {tentativas-1}\n Pressione qualquer tecla pra sair")
        break;
    elif tentativas != rondas:
        player = int(input(f"\n Na {tentativas-1}a tentativa você escolheu {player} e errou.\n Tente novamente, lembre que o intervalo é de {minimo} a {maximo}\n"))
    else:
        print(f"\nObrigado por ter jogado {nome}, mas você esgotou o nr de tentativas\n A resposta certa seria {computer}")
    
print('Jogo encerrado!')
