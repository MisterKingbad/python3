# ano de nascimento 7 pessoas maior ou menor
cont = 0
from datetime import date
ano_at = date.today().year
tot_maior = 0
tot_menor = 0
for c in range(1, 8):
    ano_nasc = int(input("Digite o ano de nascimento da {}a pessoas: ".format(c)))
    idade = ano_at - ano_nasc
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1
print('Tivemos {} pessoas maiores de idade'.format(tot_maior))
print('Tivemos {} pessoas menores de idade'.format(tot_menor))
