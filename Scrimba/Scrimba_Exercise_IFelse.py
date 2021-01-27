# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

num1 = float(input("Introduza a primeira variável"))
num2 = float(input("Introduza a segunda variável"))
operator = input("Introduza o operador correspondente \n + para adicao \n -  para subtracao \n *  para multiplicacao \n /  para divisao")

if operator == '+':
    resultado = num1 + num2
elif operator == '-':
    resultado = num1 - num2
elif operator == '*':
    resultado = num1 * num2
elif operator =='/':
    resultado = num1 / num2
else:
    resultado = print('Operador inválido')
    print('Favor introduzir um dos operadores indicados')

print(f'O resultado da operação é {resultado}')

##### https://docs.python.org/3/py-modindex.html #####