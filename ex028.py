# fazer computador pensar em um numero e ver se o usuario acertou.
from random import randint
from time import sleep
pensado = randint(1, 5)  # faz o computador sortear
print("\033[1;36m---\033[m" * 20)
print("\033[1;36mVou pensar em um numero entre 0 e 5. Tente adivinhar.")
print("\033[1;36m---\033[m" * 20)
n_digitado = int(input("\033[1;32mEm que numero pensei?:\033[m"))  # o jogador tenta adivinhar
print("\033[1;34mPROCESSANDO.....")
sleep(1)
if pensado == n_digitado:
    print(f"\033[1;30;42mVocê acertou! O numero pensado foi {pensado}\033[m")
else:
    if n_digitado < pensado:
        print(f"\033[1;30;41mVocê errou! o numero digitado {n_digitado} é menor que o numero pensado {pensado}. Computador ganha!\033[m")
    else:
        print(f"\033[1;30;41mVocê errou! o numero digitado {n_digitado} é maior que o numero pensado {pensado}. Computador ganha!\033[m")