def notas(*args, situacao=False):
	"""
	=> Recebe várias notas de um aluno e retorna:
	- A quantidade de notas recebidas
	- A maior nota
	- A menor nota
	- A média da turma
	- A situação académica (opcional)
	:param notas: recebe várias notas
	:param situacao: (opcional) mostra ou não a situação académica
	:return: dicionario com estatistica das notas (e situação académica)
	"""
	pos = total = soma = maior = menor = media = 0.00
	result = {}
	# O código de 18 a 29 pode ser substituído pelas funções:
	# len(args) -> total | max(args)/min(args) -> maior/menor
	# sum(args)/len(args) -> média
	for nota in args:
		if pos == 0:
			maior = menor = nota
		else:
			if nota > maior:
				maior = nota
			if nota < menor:
				menor = nota
		total += 1
		soma += nota
		pos += 1
	media = round(soma/total, 2)
	
	if media < 10:
		classificacao = 'REPROVADO'
	elif media >= 14:
		classificacao = 'DISPENSADO'
	else:
		classificacao = 'APROVADO'
	
	result['total'] = int(total)
	result['maior'] = maior
	result['menor'] = menor
	result['media'] = media
	
	if situacao == True:
		result['classificacao'] = classificacao
		return result
	else:
		return result


resp = notas(10, 14, 6.5, 8.5)
resp2 = notas(11, 14, 9.6, 8.3, 5.5, situacao=True)
print(resp)
print(resp2)