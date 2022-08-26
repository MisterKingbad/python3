listanum = list()
listapar = list()
listaimpar = list()
while True:
    listanum.append(int(input('Qualquer valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR?[S/N] ')).upper().strip()[0]
    if resp in 'N':
        break
for i, v in enumerate(listanum):
    if v % 2 == 0:
        listapar.append(v)
    elif v % 2 == 1:
        listaimpar.append(v)
print(f'A lista completa e {listanum}')
print(f'A lista de pares e {listapar}')
print(f'A lista de impares e {listaimpar}')