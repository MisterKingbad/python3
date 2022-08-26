lista = list()
mai = 0
men = 0
for count in range(0, 5):
    lista.append(int(input(f'digite um valor para a posicao {count}: ')))
    if count == 0:
        mai = men = lista[count]
    else:
        if lista[count] > mai:
            mai = lista[count]
        if lista[count] < men:
            men = lista[count]
print(f'voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {min(lista)} nas posicoes ', end='')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end='')