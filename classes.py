from constants import UNIDADES, DEZENAS, CENTENAS, TEENS, SINGULAR_CENTENA, SINGULAR_MILHAR





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

