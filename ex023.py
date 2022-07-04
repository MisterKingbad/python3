# de forma string nao da p fazer com 4 dijitos
"""um = int(input("Digite um numero de 0 a 1000: "))
n = str(num)
print('unidade {}'.format(n[3]))
print('dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhar {}'.format(n[0]))"""
# -------------------------------------------------------

num = int(input("Digite um numero de 0 a 1000: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))