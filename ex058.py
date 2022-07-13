from random import randint
computador = randint(0, 10)
from time import sleep
c = 1
cont = 0
while c != 10:
    resposta = int(input("DIGITE SUA RESPOSTA:"))
    cont += 1
    print("PROCESSANDO...")
    sleep(0.5)
    if resposta == computador:
        print("\033[1;30;42mPARABENS!! VOCE ACERTOU! A RESPOSTA ERA {}\033[m".format(computador))
        break
    else:
        if resposta < computador:
            print('um pouxo mais...')
        elif resposta > computador:
            print('um pouco menos...')
        print("\033[1;30;41mTENTE NOVAMENTE!\033[m")
print("\033[1;32mACABOU! Você usou {} tentativas.\033[m".format(cont))
