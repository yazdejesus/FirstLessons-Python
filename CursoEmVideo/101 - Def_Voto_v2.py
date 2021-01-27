from datetime import date

def voto(ano_nascimento=date.today().year):
	ano_actual = date.today().year
	idade = ano_actual - ano_nascimento
	if idade < 18:
		elegibilidade = 'NAO PODE VOTAR'
	elif idade > 65:
		elegibilidade = 'VOTO OPCIONAL'
	else:
		elegibilidade = 'VOTO OBRIGATORIO'
	return idade, elegibilidade


ano_votante = int(input("Digite o seu ano de nascimento: "))

idade_votante = voto(ano_votante)[0]
situacao_votante = voto(ano_votante)[1]
print(f'Com {idade_votante} anos: {situacao_votante}')