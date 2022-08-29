pessoas = list()
dados = list()
mai = men = 0
p_c = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    p_c += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Foram cadastradas {p_c} pessoas.')
print(f'O maior peso foi de {mai}.0Kg. Peso de ', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(f'[{p[0]}] ', end=' ')
print()
print(f'O menor peso foi de {men}.0Kg. peso de ', end=' ')
for p in pessoas:
    if p[1] == men:
        print(f'[{p[0]}] ', end=' ')
