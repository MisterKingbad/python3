umate20 = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input("digite um valor de 0 ate 20: "))
    if n < 0 or n > 20:
        print('valor invalido. Tente novamente.')
    print(f'VOCE DIGITOU O NUMERO "{umate20[n]}"')

