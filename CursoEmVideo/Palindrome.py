texto = input('Digite uma frase: ')
caracteres = list("".join(texto.split()))
#print(caracteres)
reversa = caracteres[::-1]
#print(reversa)
if caracteres == reversa:
    print('é palindrome')
else:
    print('nao é palindrome')