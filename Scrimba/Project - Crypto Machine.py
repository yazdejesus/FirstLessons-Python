keys = 'abcdefghijklmnopqrstuvwxyz- !'
values = keys[::-1]

dict_e = dict(zip(keys,values))
dict_d = {value:key for key,value in dict_e.items()}

msg = input("Introduza a mensagem a encriptar:").lower()
mode = input("Seleccione o modo: \n e => encriptar \n d => desencriptar").lower()

try:
    if mode == 'e':
        new_msg = ''.join([dict_e[x] for x in msg])
    elif mode == 'd':
        new_msg = ''.join([dict_d[x] for x in msg])
    print(new_msg.capitalize())
except KeyError as e:
    print('caracter inválido: ',{e})