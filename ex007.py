m1 = float(input('media 1: '))
m2 = float(input('media 2: '))
mt = (m1 + m2) / 2
print('a media total foi {:.1f}'.format(mt))

if mt >= 5:
    print("aprovado.")
else:
    print('reprovado')
