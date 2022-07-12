sx = 'M', "F"

while sx == 'M' or 'F':
    sx = str(input("DIGITE O SEXO M/F:")).upper()
    if sx in 'Mm' and 'Ff':
        print(' VOCE ESCOLHEU "{}"'.format(sx))
        break
    else:
        print("TENTE NOVAMENTE")