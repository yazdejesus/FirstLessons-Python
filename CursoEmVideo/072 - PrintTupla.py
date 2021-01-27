#criar tuple de 0 a 20, ler nr e responder o valor por extenso
num = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez")
ler = 11

if ler not in range(0,10):
	ler = int(input("Digite um nr de 0 a 10: "))

print(f"você digitou o número {num[ler]}")