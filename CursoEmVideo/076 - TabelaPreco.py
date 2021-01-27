precario = ("lápis", 1.75, "borracha", 2, "caderno", 15.9, "estojo", 25)

print(f"{'-'*40}\n{'LISTAGEM DE PREÇOS':^40}\n{'-'*40}")
#print("-"*30,"\n","LISTAGEM DE PREÇOS\n","-"*30)
for n in precario:
    if type(n) == str:
        #print(f"{n:<10}{'.'*20}{'R$'}", end="")
        #existem formas melhores para imprimir o texto formatado
        #basta depois dos : colocar o caracter que irá preencher o espaço
        print(f"{n:.<30}{'R$'}", end="")
    elif type(n) == int or type(n) == float:
        print(f"{n:>8.2f}")
print(f"{'-'*40}")