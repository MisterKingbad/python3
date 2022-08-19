from random import randint

v = 0
print('=-' * 30)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 30)
while True:
    valor = int(input('diga um valor: '))
    computa = randint(0, 10)
    total = valor + computa
    tipo = ' '
    while tipo not in 'PpIn':
        tipo = str(input('PAR OU IMPAR? [P/I]')).strip().upper()[0]
    print(f'voce jogou {valor} e o Computador jogou {computa}. total de {total} ', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('VOCE GANHOU!')
            v += 1
        else:
            print('VOCE PERDEU!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE GANHOU!')
            v += 1
        else:
            print('VOCE PERDEU!!')
            break
    print('vamos jogar novamente....')
print(f'GAME OVER!! VOCE VENCEU {v} VEZES.')
