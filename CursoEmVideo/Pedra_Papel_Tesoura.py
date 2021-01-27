#Project Pedra-Papel-Tesoura
from random import choice

opcoes = {0:'sair', 1:'pedra',2:'papel',3:'tesoura'}
opcoes_pc = {1:'pedra',2:'papel',3:'tesoura'}

vitorias = empates = derrotas = 0

try:
    escolha = int(input("Bem vindo ao Pedra-Papel-Tesoura. \n O que vais escolher?\n Digite 1 para Pedra, 2 para Papel, 3 para Tesoura, 0 para sair:\n "))
    humano = opcoes[escolha]

    rondas = 0

    while escolha != 0:
        computer_run = choice(list(opcoes_pc))
        computer = opcoes_pc[computer_run]
        if escolha == computer_run:
            escolha = int(input(f"Ronda {rondas+1}: Empate.\n Escolheste {humano} e o computador também escolheu {computer}.\n \n Digite 1 para Pedra, 2 para Papel, 3 para Tesoura, 0 para sair:\n "))
            humano = opcoes[escolha]
            empates += 1
        elif escolha-computer_run == 1:
            escolha = int(input(f"Ronda {rondas+1}: Vitória.\n Escolheste {humano} e o computador escolheu {computer}.\n \n Digite 1 para Pedra, 2 para Papel, 3 para Tesoura, 0 para sair:\n "))
            humano = opcoes[escolha]
            vitorias += 1
        elif escolha-computer_run == -2:
            escolha = int(input(f"Ronda {rondas+1}: Vitória.\n Escolheste {humano} e o computador escolheu {computer}.\n \n Digite 1 para Pedra, 2 para Papel, 3 para Tesoura, 0 para sair:\n "))
            humano = opcoes[escolha]
            vitorias += 1
        else:
            escolha = int(input(f"Ronda {rondas+1}: Perdeste!\n Escolheste {humano} e o computador escolheu {computer}.\n \n Digite 1 para Pedra, 2 para Papel, 3 para Tesoura, 0 para sair:\n "))
            humano = opcoes[escolha]
            derrotas += 1
        rondas += 1
except KeyError as ke:
    print('Por favor seleccione um valor entre 0 e 3. Valor seleccionado: ',ke)

print(f"\n ***Obrigado por jogar connosco***\n Ao fim de {rondas} rondas ganhaste {vitorias}. empataste {empates}. e perdeste {derrotas}.\n Percentagem de vitorias: ",(vitorias/rondas*100),'%')


# tesoura ganha papel (3-2=1)
# papel ganha pedra (2-1=1)
# pedra ganha tesoura (1-3=-2)
# tesoura perde para pedra (3-1=2)
# papel perde para tesoura (2-3=-1)
# pedra perde para papel (1-2=-1)