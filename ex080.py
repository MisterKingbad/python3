lista = list()
for c in range(0, 5):
    n = (int(input(f'Digite o {c}o numero: ')))
    if c == 0:
        lista.append(n)
        print('adicionado ao final da lista...')
    elif n > lista[len(lista)-1]:
        lista.append(n)
        print('adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posicao {pos} da lista...')
                break
            pos += 1
print(f'os valore digitados em ordem foram {lista}')