from datetime import date

def calcula_idade(ano_nascimento=date.today().year):
	"""
	=> Funcao calcula idade do votante
	param ano_nascimento: ano de nascimento do votante
	default value: ano corrente
	return: retorna idade do votante
	"""
	idade = ano_actual - ano_nascimento
	return idade

def voto(idade=0):
	"""
	=> Funcao calcula elegibilidade do votante
	param idade: recebe a idade do votante
	default value: 0
	return: retorna elegibilidade do votante
	"""
	if idade < 18:
		elegibilidade = 'NAO PODE VOTAR'
	elif idade > 65:
		elegibilidade = 'VOTO OPCIONAL'
	else:
		elegibilidade = 'VOTO OBRIGATORIO'
	return elegibilidade


ano_actual = date.today().year
ano_votante = int(input("Digite o seu ano de nascimento: "))

idade_votante = calcula_idade(ano_votante)
situacao_votante = voto(age)
print(f'Com {idade_votante} anos: {situacao_votante}')