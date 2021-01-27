x = input("Digite uma expressão: ")
lista = list(x.strip())
#print(x)
#print(lista)

if lista.count('(') == lista.count(')'):
    print("Pelo nr de parenteses, a expressao é válida")
else:
    print("Pelo nr de parenteses, a expressao é inválida")

#a solucao proposta é bem diferente
# pegar na expressão, iterar por ela e
# se encontrar um parenteses aberto, adicionar o parenteses à lista
# e se encontrar um parentes fechado verificar se a lista está vazia
# se estiver vazia, adicionar um parenteses fechado à lista 
# e se nao estiver vazia, remover um parenteses aberto da lista
# se no final dessa iteracao a lista estiver vazia, entao a expressao ta ok.
