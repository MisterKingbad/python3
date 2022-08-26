from time import sleep
valor = list()
while True:
    v = int(input('digite qualquer valor: '))
    if v not in valor:
        valor.append(v)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado! Nao adicionado... ')
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('QUER CONTINUAR? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print(f'voce digitou os valores {sorted(valor)}')



