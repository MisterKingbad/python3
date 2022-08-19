from random import randint
while True:
    valor = int(input('digite um valor: '))
    comp = randint(0,10)
    tot = valor + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR? [P/I]'))
