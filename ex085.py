lista = []
par = []
impoar = []
for c in range(0, 7):
    lista.append(int(input(f'digite o {c+1}o. valor: ')))
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impoar.append(v)
print(f'Os valores pares digitados foram: {sorted(par)}')
print(f'Os valores impares digitados foram: {sorted(impoar)}')