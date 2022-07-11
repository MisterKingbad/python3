import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
computador = random.randint(0,2)
jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(0.5)
print("-="*11)
print(f"Computador jogou '{itens[computador]}'")
print(f" jogador jogou '{itens[jogada]}'")
print('-='*11)
if computador == 0: # computador jogou pedra
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print("JOGADOR VENCE")
    elif jogada == 2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA!")
elif computador == 1: # computador jogou papel
    if jogada == 0:
        print('COMPUTADOR VENCE')
    elif jogada == 1:
        print("EMPATE")
    elif jogada == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA!")
elif computador == 2: # computador jogou tesoura
    if jogada == 0:
        print("JOGADOR VENCE")
    elif jogada == 1:
        print("COMPUTADOR VENCE")
    elif jogada == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA")
