import sys

DIGIT_MAP = {
	'zero': '0',
	'um': '1',
	'dois': '2',
	'três': '3',
	'quatro': '4',
	'cinco': '5',
	'seis': '6',
	'sete': '7',
	'oito': '8',
	'nove': '9',
}

'''
primeira forma de tratar excepções
def converter(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
	except (KeyError, TypeError):
        pass #alternativamente return -1
'''

#segunda forma de tratar excepções
def converter(s):
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
	except (KeyError, TypeError) as e:
        print(f "Conversion error: {e!r}",
                file=sys.stderr)
        return -1