from datetime import date
from time import sleep

cadastro = dict()

while True: #também pode ser feito sem loop basta (ver comentario no if)
    cadastro["nome"] = input("Nome: \t\t\t\t\t")
    ano_nasc = int(input("Ano de Nascimento: \t\t\t"))
    idade = date.today().year - ano_nasc #também funciona com datetime.now().year
    cadastro["idade"] = idade
    cadastro["carteira"] = int(input("Carteira de Trabalho (0 se não tiver):\t"))
    if cadastro["carteira"] == 0: #pode-se colocar o resto do programa dentro do if
        break;                    #basta colocar a condicao inversa...if != 0
    cadastro["contratacao"] = int(input("Ano de contratacao: \t\t\t"))
    cadastro["salario"] = float(input("Salario: \t\t\t\t"))
    cadastro["aposentadoria"] = (cadastro["contratacao"] - ano_nasc) + 35
    break;

print('-='*25)

for x,y in cadastro.items():
    sleep(1)
    print(f"\t - {x} tem o valor {y}")