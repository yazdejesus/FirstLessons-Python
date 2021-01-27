def calcula_area(largura, comprimento):
	area = largura * comprimento
	print(f'A área de um terreno {largura:.2f}x{comprimento:.2f} é de {area:.2f}m2.')


print('-'*40)
print('          CONTROLE DE TERRENOS')
print('-'*40)

lar = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
calcula_area(lar,comp)