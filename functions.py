from constants import CENTENAS, IRREGULAR, TEENS, DEZENAS, UNIDADES


def _milhao(string):  # sourcery no-metrics
    lista = str(string).zfill(9)
    milhao, milhar, centena = (
        [lista[0], lista[1], lista[2]],
        [lista[3], lista[4], lista[5]],
        [lista[6], lista[7], lista[8]],
    )
    new_list = [milhao, milhar, centena]
    res = ""

    lista = new_list[0]  # CENTENA
    for index, i in enumerate(lista):
        if index == 0:
            if i != "1" and lista[1] == "0" and lista[2] == "0":
                res += f"{CENTENAS[int(i)]}"
            elif i == "1" and lista[1] == "0" and lista[2] == "0":
                res += f"{IRREGULAR[1]}"
            elif lista[0] == "0":
                res += f""
            else:
                res += f"{CENTENAS[int(i)]} e "

        elif index == 1:
            if i == "0":
                res += f""
            elif i == "1":
                concat = str(i) + str(lista[1])
                res += f"{TEENS[int(concat)]} milhões "
                break
            else:
                res += f"{DEZENAS[int(i)]} "

        elif index == 2:
            if i == "1" and lista[0] == "0" and lista[1] == "0":
                res += f"{UNIDADES[int(i)]} milhão "
            elif i != "0":
                res += f"{UNIDADES[int(i)]} milhões "
            else:
                res += f"e {UNIDADES[int(i)]} milhões "

    lista = new_list[1]  # DEZENA
    for index, i in enumerate(lista):
        if index == 0:  # 1
            if i != "1" and lista[1] == "0" and lista[2] == "0":
                res += f"{CENTENAS[int(i)]} "
            elif i == "1" and lista[1] == "1" and lista[2] == "1":
                res += f"{CENTENAS[1]} e "
            else:
                res += f"e {CENTENAS[int(i)]} e "

        elif index == 1:  # 2
            if i == "0":
                res += f""
            elif i == "1":
                concat = str(i) + str(lista[2])
                res += f"{TEENS[int(concat)]} "
            else:
                res += f"{DEZENAS[int(i)]} e "

        elif index == 2:  # 4
            if i == "1" and lista[2] == "1" and lista[1] == "1":
                res += ""
            elif i != "0":
                res += f""
            if i == "0":
                res += f""
            else:
                res += f"{UNIDADES[int(i)]} mil e "

    lista = new_list[2]  # UNIDADE
    for index, i in enumerate(lista):
        if index == 0:
            if lista[1] == "0" and lista[2] == "0":
                if i == "1":
                    res += f"{IRREGULAR[1]}"
                else:
                    res += f"{CENTENAS[int(i)]}"
            elif i == "1":
                res += f"{CENTENAS[int(i)]}"
            else:
                res += f"{CENTENAS[int(i)]} e "

        elif index == 1:
            if i == "0":
                res += f""
            elif i == "1":
                concat = str(i) + str(lista[2])
                res += f"{TEENS[int(concat)]} reais"
                break
            if lista[2] == "0":
                res += f"{DEZENAS[int(i)]} reais"
                break
            else:
                res += f"{DEZENAS[int(i)]} e "

        elif index == 2:
            if i == "1":
                res += f"{UNIDADES[int(i)]} reais "
            elif i == "0" and lista[1] == "0" and lista[2] == "0":
                res += f"e{CENTENAS[int(i)]} reais"
            elif i != "0" and lista[1] == "0" and lista[2] == "0":
                res += f"e {UNIDADES[int(i)]}"
            else:
                res += f"{UNIDADES[int(i)]} reais"

    return res


def _milhar(string):  # sourcery no-metrics
    lista = str(string).zfill(9)
    milhao, milhar, centena = (
        [lista[0], lista[1], lista[2]],
        [lista[3], lista[4], lista[5]],
        [lista[6], lista[7], lista[8]],
    )
    new_list = [milhao, milhar, centena]
    res = ""

    lista = new_list[1]  # DEZENA
    for index, i in enumerate(lista):
        if index == 0:
            if i == "1" and lista[1] == "0" and lista[2] == "0":
                res += f"{IRREGULAR[int(i)]} mil e "
                break
            if lista[1] == "0" and lista[2] == "0":
                res += f"{CENTENAS[int(i)]} mil"
                break
            elif lista[0] == "0":
                res += f""
            else:
                res += f"{CENTENAS[int(i)]} e "

        elif index == 1:
            if i == "0":
                res += f""
            elif i == "1":
                concat = str(i) + str(lista[2])
                res += f"{TEENS[int(concat)]} mil "
                break
            else:
                res += f"{DEZENAS[int(i)]} e "

        elif index == 2:
            if i != "0":
                res += f"{UNIDADES[int(i)]} mil "

    lista = new_list[2]  # UNIDADE
    for index, i in enumerate(lista):
        if index == 0:
            if i == "1":
                res += f"{CENTENAS[int(i)]} e "
            elif lista[0] == "0" and lista[1] == "0" and lista[2] == "0":
                res += f" reais"
                break
            elif lista[1] == "0" and lista[2] == "0":
                res += f"{CENTENAS[int(i)]} reais"
                break
            elif lista[1] == "0":
                res += f""

            else:
                res += f"{CENTENAS[int(i)]} e "

        elif index == 1:
            if i == "0":
                res += f""
            elif i == "1":
                concat = str(i) + str(lista[2])
                res += f"{TEENS[int(concat)]} reais"
                break
            else:
                res += f"{DEZENAS[int(i)]} e "

        elif index == 2:
            if lista[1] != "1" and lista[2] != "1":
                res += f"{UNIDADES[int(i)]}"
            if lista[0] == "0" and lista[1] == "0" and i == "1":
                res += "mil"
            else:
                res += f" reais"

    return res


def _reais(string):  # sourcery no-metrics
    lista = str(string).zfill(9)
    milhao, milhar, centena = (
        [lista[0], lista[1], lista[2]],
        [lista[3], lista[4], lista[5]],
        [lista[6], lista[7], lista[8]],
    )
    new_list = [milhao, milhar, centena]
    res = ""

    lista = new_list[2]  # UNIDADE
    for index, i in enumerate(lista):
        if index == 0:
            if lista[1] == "0" and lista[2] == "0":
                res += f"{IRREGULAR[int(i)]}" if i == "1" else f"{CENTENAS[int(i)]}"
            elif lista[0] == "0":
                res += f""

            else:
                res += f"{CENTENAS[int(i)]} e "

        elif index == 1:
            if i == "0":
                res += f""
            elif i == "1":
                concat = str(i) + str(lista[2])
                res += f"{TEENS[int(concat)]} reais"
                break
            elif lista[0] == "0" and lista[2] == "0":
                res += f"{DEZENAS[int(i)]} reais"
                break
            elif lista[2] == "0":
                res += f"{DEZENAS[int(i)]}"
            else:
                res += f"{DEZENAS[int(i)]} e "

        elif index == 2:
            if i == "1" and lista[0] == "0" and lista[1] == "0":
                res += "um real"
            elif i == "0":
                res += " reais"
            else:
                res += f"{UNIDADES[int(i)]} reais"

    return res
