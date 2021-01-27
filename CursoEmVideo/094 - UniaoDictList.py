#ler nome, sexo(m/f) e idade até o user digitar N para parar (perguntar sempre)
#mostrar a)total de registros, b)média de idade c) mulheres reg d)lista dos acima da media de idade
#a lista em D deve mostrar assim nome = <A> ; sexo = <B>; idade=<C>
#PS: Ao contrario do exercicio anterior, aqui o dict deve estar dentro da lista
#[{a,b,c},{a,b,c},{a,b,c,},{a,b,c},{a,b,c}]

cadastro = list()
while True:
    temp = dict()
    temp["nome"] = input("Nome:\t\t").title()
    while True:
        temp["sexo"] = input("Sexo (M/F):\t").upper()
        if temp["sexo"] in "MF":
            break
        print("ERRO! Digite apenas M ou F")
    temp["idade"] = int(input("Idade:\t\t"))
    cadastro.append(temp.copy())
    temp.clear()
    while True:
        stop = input("Quer continuar? (S/N) ").upper()
        if stop in "SN":
            break
        print("ERRO! Digite S para continuar e N para parar")
    if stop == 'N':
        break
    print()
print('-='*30)
print(f"A) Ao todo temos {len(cadastro)} pessoas registradas")

soma = 0 #Para economizar processamento, fazer a soma à cada iteração do while anterior
for i in range(0,len(cadastro)):
    soma += cadastro[i]["idade"]
media = soma / len(cadastro)
print(f"B) A média de idade é de {media} anos")

print(f"C) As mulheres registradas foram: ", end="")
for i in range(0,len(cadastro)):#melhor for seria for p in cadastro: if cadastro['sexo']...
    if cadastro[i]["sexo"] == "F":
        print(cadastro[i]["nome"], end=" ")
print()
        
print(f"D) A lista de pessoas que estão acima da média:")
for i in range(0,len(cadastro)): #again iterar sobre a lista, para depois da condição
    if cadastro[i]["idade"] > media: #voltar a iterar sobre o dicionario (for k,v in i.items()/:
        print(f"\tnome = {cadastro[i]['nome']}\t sexo = {cadastro[i]['sexo']}\t idade = {cadastro[i]['idade']}")
print('-='*27,'*FIM*')
