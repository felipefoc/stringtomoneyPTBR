from constants import UNIDADES, DEZENAS, CENTENAS, TEENS, SINGULAR_CENTENA, SINGULAR_MILHAR



class Reais:
    def __init__(self, number):
        self.number = number
        self.lenght = len(number)
        self.full_number = int(number)
        self.first_number = int(self.number[-1])
        try:
            self.second_number = int(self.number[-2])
            self.third_number = int(self.number[-3])
            self.fourth_number = int(self.number[-4])
            self.fifth_number = int(self.number[-5])
            self.sixth_number = int(self.number[-6])
            self.seventh_number = int(self.number[-7])
        except IndexError:
            pass
        self.prefix_sing = 'real'
        self.sufix = 'reais'


    def reais_to_extense(self):
        if self.lenght <= 1:            
            if self.first_number == 0:
                return ''
            elif self.first_number == 1:
                return f'{UNIDADES[self.first_number]} {self.prefix_sing}'
            return f'{UNIDADES[self.first_number]} {self.sufix}'
        elif self.lenght <= 2:
            if self.first_number == 0:
                return f'{DEZENAS[self.full_number]} {self.sufix}'
            elif self.second_number == 1:
                return f'{TEENS[self.full_number]} {self.sufix}'
            return f'{DEZENAS[self.second_number*10]} e {UNIDADES[self.first_number]} {self.sufix}'
        elif self.lenght <= 3:
            if self.third_number == 1 and self.number[-2:] == '00':
                return f'{SINGULAR_CENTENA[self.third_number]} {self.sufix}'
            elif self.second_number == 1:
                return f'{CENTENAS[self.third_number]} e {TEENS[int(self.number[-2:])]} {self.sufix}'
            return f'{CENTENAS[self.third_number]} e {DEZENAS[self.second_number*10]} e {UNIDADES[self.first_number]} {self.sufix}'
        elif self.lenght <= 4:
            if self.fourth_number == 1 and self.number[-3:] == '000':
                return f'{SINGULAR_MILHAR[self.fourth_number]} {self.sufix}'
            elif self.second_number == 1:
                return f'{UNIDADES[self.fourth_number]} mil {CENTENAS[self.third_number]} e {TEENS[int(self.number[-2:])]} {self.sufix}'
            return f'{UNIDADES[self.fourth_number]} mil {CENTENAS[self.third_number]} e {DEZENAS[self.second_number*10]} e {UNIDADES[self.first_number]} {self.sufix}'
        elif self.lenght <= 5:
            if self.fifth_number == 1 and self.number[-4:] == '0000':
                return f'{DEZENAS[int(self.number[:2])]} mil {self.sufix}'
            elif self.fifth_number == 1 and self.second_number == 1:
                return f'{TEENS[int(self.number[:2])]} mil {CENTENAS[self.third_number]} e {TEENS[int(self.number[-2:])]} {self.sufix}'
            elif self.second_number == 1:
                return f'{DEZENAS[int(self.number[:2])]} mil {CENTENAS[self.third_number]} e {TEENS[int(self.number[-2:])]} {self.sufix}'
            return f'{DEZENAS[int(self.number[:2])]} mil {CENTENAS[self.third_number]} e {DEZENAS[self.second_number*10]} {self.sufix}'
        elif self.lenght <= 6:
            if self.sixth_number == 1 and self.number[-5:] == '00000':
                return f'{SINGULAR_CENTENA[self.sixth_number]} mil {self.sufix}' 
            return f'{CENTENAS[self.sixth_number]} e {'

            


class Cents:
    def __init__(self, dezenas): #50
        self.first_number = int(dezenas[-2])
        self.second_number = int(dezenas[-1])
        self.full_number = int(dezenas[-2:])
        self.sufix = 'centavos'

            
    def dezenas_to_extense(self):
        if self.first_number == 00:
            return ''
        elif self.first_number == 0 and self.second_number == 0:                                              # XXXX.00
            return f'e {UNIDADES[self.first_number]}'
        elif self.first_number == 0:                                                                        # XXXX.0{VAR}
            return f'e {UNIDADES[self.second_number]} {self.sufix}'
        elif self.first_number == 1 and self.second_number != 0:                                            # XXXX.1{VAR}
            return f'e {TEENS[self.full_number]} {self.sufix}'
        elif self.second_number == 0:                                                                       # XXXX.{VAR}0
            return f'e {DEZENAS[self.full_number]} {self.sufix}'
        else:                                                                                               # XXXX.{VAR}{VAR}
            return f'e {DEZENAS[self.first_number*10]} e {UNIDADES[self.second_number]} {self.sufix}'


       

class Money:
    def __init__(self, number):
        self.full_number = number
        self.before_comma = number.split(',')[0]
        self.after_comma = number.split(',')[1]

