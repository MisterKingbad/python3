lista = list()
for count in range(0, 5):
    lista.append(int(input(f'digite um valor para a posicao {count}: ')))
    count += 1
print(f'voce digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posicoes ', end=' ')
if max(lista) in lista:
    print(lista.index(max(lista)), end='...')

print(f'\nO menor valor digitado foi {min(lista)} nas posicoes', end=' ')
if min(lista) in lista:
    print(lista.index(min(lista)), end='...')
