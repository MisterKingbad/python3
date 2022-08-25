umate20 = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
resp = ' '
while True:

    n = int(input("digite um valor de 0 ate 20: "))
    if 0 <= n <= 20:
        break
    print('valor invalido. Tente novamente.',end=' ')

print(f'VOCE DIGITOU O NUMERO "{umate20[n]}"')

