lista = list()
c = 0
while True:
    c += 1
    lista.append(int(input('coloque qualquer valor:')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUER CONTINUAR?[S/N]')).upper().strip()[0]
    if resp in 'N':
        break
print(f'Foram digitados {c} numeros')
print(f'Os valores em ordem decrescente sao ', end='')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print(f'o valor 5 faz parte da lista!')
else:
    print('o valor 5 nao faz parte da lista.')