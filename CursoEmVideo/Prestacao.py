casa = float(input('Qual o valor da sua casa? MZN_'))
salario = float(input('Qual o seu salário mensal líquido? MZN_'))
anos = int(input('Em quantos anos pretendes pagar o empréstimo? '))

valor_prestacao = casa/(anos*12)

if valor_prestacao >= salario*0.3:
	print('Emprestimo negado')
else:
	print(f'Emprestimo aceite, a sua prestacao sera de {valor_prestacao}')
