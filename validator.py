def validate_line(line):  # sourcery skip: return-identity
    line = line.replace('/n', '')
    try:
        splited_line = line.split(',')
        if len(splited_line[1]) == 2 and len(splited_line[0])<=9:
            return True
        return False
    except IndexError:
        return False
