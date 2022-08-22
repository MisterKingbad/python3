from random import randint
while True:
    v = 0
    valor = int(input('digite um valor: '))
    comp = randint(0,10)
    tot = valor + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR? [P/I]')).upper().strip()[0]
        print(f'Voce jogou {valor} e o camputador jogou {comp}, total e {tot}', end=' ')
        print('DEU PAR!'if tot % 2 == 0 else 'DEU IMPAR!')
        if tipo == 'P':
            if tot % 2 == 0:
                print('Voce ganhou!!!')
                v += 1
            else:
                print('Voce perdeu!!!')
                break
        if tipo == 'I':
            if tot % 2 == 1:
                print('Voce ganhou!!!')
                v += 1
            else:
                print('Voce perdeu!!!')
                break
    print('VAMOS J0GAR NOVAMENTE...')
print(f'GAME OVER! Voce venceu {v} vezes')
