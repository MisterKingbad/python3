from time import sleep
valor = list()
while True:
    valor.append(int(input('digite qualquer valor: ')))
    sleep(1)
    if valor in valor:
        print('valor duplicado.')
        valor.remove(valor)
    else:
        print('valor adicionado com sucesso...')
    sleep(1)


    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('QUER CONTINUAR? [S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print(f'voce digitou os valores {valor}')



