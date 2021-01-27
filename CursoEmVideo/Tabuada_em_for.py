nr = int(input("Digite um nr para ver a sua tabuada: "))
star = '-'
print(f'\n{star*12:^15}')
for i in range(1,11):
    if i!=10:
        print(f'{nr} x  {i}  = {nr*i}', end="\n")
    else:
        print(f'{nr} x {i}  = {nr*i}', end="\n")

print(f'{star*12:^15}')