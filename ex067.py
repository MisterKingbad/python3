print('============================================')
tb = int(input("QUER VER A TABUADA DE QUAL VALOR?"))
print('============================================')
c = 1
while c < 10+1:
    if tb <= -0:
        break
    print('{} x {:2} = {}'.format(tb, c, tb * c))
    c += 1