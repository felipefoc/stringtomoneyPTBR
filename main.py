# -*- coding: utf-8 -*-


# Autor: Felipe Machado Fernandes Mayer

"""
## ToDo

- Receber txt # Done
- ler linha do txt # Done
- Aceitar apenas no formato XXXX.XX # Done
- Aceitar até 9 digitos antes da virgula e 2 após # Done
- Transformar os centavos por extenso # Done
- Trasformar os primeiros 4 digitos por extenso
"""


from validator import validate_line
from classes import Cents, Money, Reais 
    
    # fix number='10000,00'

arg = Money(
    number='100000,14'
)

print(f'BEFORE_COMMA:{arg.before_comma} AFTER_COMMA:{arg.after_comma} FULL_NUMBER:{arg.full_number}')
calc = Cents(
    dezenas=arg.after_comma
)
calc2 = Reais(
    number=arg.before_comma
)


print(f'{calc2.reais_to_extense()} {calc.dezenas_to_extense()}')


if len(arg.before_comma) >= 7:
    centena(arg.before_comma)





### read doc
# document = open("document.txt", "r")
# for line in document:
#     line = line.strip()
#     if validate_line(line):
#         value = Money(line)
#         print(value.before_comma, value.after_comma, value.full_number)
#     else:
#         print(f'{line} invalida')
   
    