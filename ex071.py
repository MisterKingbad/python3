from time import sleep
print('='*25)
print('{:^25}'.format('BANCO'))
print('='*25)
valor = int(input('Que valor voce quer sacar? R$'))
tot = valor
ced = 50
totced = 0
while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break
