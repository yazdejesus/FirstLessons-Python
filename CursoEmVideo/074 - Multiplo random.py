from random import sample, randint

tupla_num = sample(list(range(0,10)), 5)
print(f"Os numeros gerados foram {tupla_num}\nO maior numero foi {max(tupla_num)} e o menor numero foi {min(tupla_num)}")


#forma alternativa de fazer seria:
numeros = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f"\nTambém gerei {numeros}\nO maior numero foi {max(numeros)} e o menor numero foi {min(numeros)}")


#nota: usando sample não temos duplicados, mas usando múltiplos randint temos
