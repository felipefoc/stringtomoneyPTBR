# -*- coding: utf-8 -*-


# Autor: Felipe Machado Fernandes Mayer

"""
## ToDo

- Receber txt # Done
- ler linha do txt # Done
- Aceitar apenas no formato XXXX.XX # Done
- Aceitar até 9 digitos antes da virgula e 2 após # Done
- Transformar os centavos por extenso # Done
- Trasformar os primeiros 4 digitos por extenso # Done
"""


from os import device_encoding
from validator import validate_line
from classes import Cents, Money
from functions import _milhao, _milhar, _reais


def main():
    document = open("document.txt", "r")
    for line in document:
        line = line.strip()
        if validate_line(line):
            value = Money(line)
            cents = Cents(value.after_comma).cents_extense()
            if len(value.before_comma) < 4:
                left_side = _reais(value.before_comma)
            elif len(value.before_comma) > 3 and len(value.before_comma) < 7:
                left_side = _milhar(value.before_comma)
            elif len(value.before_comma) > 6:
                left_side = _milhao(value.before_comma)
            print(f"{line} = {left_side} {cents}")
        else:
            print(f"{line} invalida/não suportadada")


if __name__ == "__main__":
    main()
