# ano bissexto
from datetime import date
ano = int(input("\033[1;4;33mEm que ano estamos?:\033[m"))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"\033[1;30;42mO ano {ano} é bissexto.")
else:
    print("\033[1;30;41mO ANO {} NÃO É BISSEXTO!".format(ano))