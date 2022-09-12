from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('      JOGO NA MEGA SENA')
print('-'*30)
quant = int(input('Quantos jogos voce quer que eu sorteie: '))
tot = 1
c = 0
while tot <= quant:
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f" Os numeros sorteados foram {jogos}", end='')
print()