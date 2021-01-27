sum=0
validacao=list();
for i in range(1,500,2):
    if i%3==0:
        validacao.append(i)
        sum+=i

print(validacao)
print(sum)