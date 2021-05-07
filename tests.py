txt = '498498448'

lista = txt.zfill(9)

milhao, milhar, centena = [lista[0], lista[1], lista[2]], [lista[3], lista[4], lista[5]], [lista[6], lista[7], lista[8]]

null = ['0','0','0']

new_list = [milhao, milhar, centena]

# IF NULL && NAO TER OUTRO VALOR != 0 NO INDEX: 


print(new_list)

UNIDADES = {
	0:'',
    1:'um',
    2:'dois',
    3:'três',
    4:'quatro',
    5:'cinco',
    6:'seis',
    7:'sete',
    8:'oito',
    9:'nove',
}
DEZENAS = {
    0: '',
    1: 'dez',
    2: 'vinte',
    3: 'trinta',
    4: 'quarenta',
    5: 'cinquenta',
    6: 'sessenta',
    8: 'setenta',
    8: 'oitenta',
    9: 'noventa',
}
TEENS = {
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
}
CENTENAS ={
	0: '',
    1: 'cento',
    2: 'duzentos',
    3: 'trezentos',
    4: 'quatrocentos',
    5: 'quinhentos',
    6: 'seiscentos',
    7: 'setecentos',
    8: 'oitocentos',
    9: 'novecentos',
}
IRREGULAR = {
    1: 'cem',
}


res = ''




lista = new_list[0] # CENTENA
for index, i in enumerate(lista):
    if index == 0:
        if i != '1' and lista[1] == "0" and lista[2] == "0":
            res += f'{CENTENAS[int(i)]}'
        elif i == '1' and lista[1] == "0" and lista[2] == "0":
            res += f'{IRREGULAR[1]}'
        else:
            res += f'{CENTENAS[int(i)]} e '

    elif index == 1:
        if i == '0':
            res += f''
        elif i == '1':
            concat = str(i) + str(lista[2])
            res += f'{TEENS[int(concat)]} milhões e '
        
        else:
            res += f'{DEZENAS[int(i)]} e '

    elif index == 2:
        res += f'um milhões ' if i == '1' else f'{UNIDADES[int(i)]} milhões e '

lista = new_list[1] # DEZENA
for index, i in enumerate(lista):
    if index == 0:
        if lista[1] == "0" and lista[2] == "0":
            res += f'{CENTENAS[int(i)]}'
        else:
            res += f'{CENTENAS[int(i)]} e '

    elif index == 1:
        if i == '0':
            res += f''
        elif i == '1':
            concat = str(i) + str(lista[2])
            res += f'{TEENS[int(concat)]} mil e '
        else:
            res += f'{DEZENAS[int(i)]} '

    elif index == 2:
        res += f'mil ' if i == '1' else f'{UNIDADES[int(i)]} mil e '
        if i == '0':
            res += f''

lista = new_list[2] # UNIDADE
for index, i in enumerate(lista):
    if index == 0:
        if lista[1] == "0" and lista[2] == "0":
            res += f'{IRREGULAR[1]}'
        else:
            res += f'{CENTENAS[int(i)]} e '

    elif index == 1:
        if i == '0':
            res += f''
        elif i == '1':
            concat = str(i) + str(lista[2])
            res += f'{TEENS[int(concat)]} reais'
            break
        else:
            res += f'{DEZENAS[int(i)]} e '

    elif index == 2:
        res += f'reais ' if i == '1' else f'{UNIDADES[int(i)]} reais '



print(res)