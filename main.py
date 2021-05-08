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

import sys
import os
import argparse
from validator import validate_line
from classes import Cents, Money
from functions import _milhao, _milhar, _reais


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Retorn the value in extense (pt-Br)')
    parser.add_argument('-i', '--input', type=str,
                    help='Path to the input directory.',
                    required=True)
    parser.add_argument('-o', '--output', type=str,
                    help='Path to the output that contains the resumes.',
                    required=True)
    return parser


def main():
    input_path = args.input
    output_path = args.output
    
    with open(input_path, "r") as document, open(f'{output_path}', "w+") as output:
        output_file = []
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
                output_file.append(f"{line} = {left_side} {cents} \n")
            else:
                if line != '':
                    output_file.append(f"{line} invalida/não suportadada \n")
        output.writelines(output_file)


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    args = arg_parser.parse_args()
    main()
