produ = ('lapis', 1.75,
         'borracha', 2.00,
         'caderno', 15.90,
         'estojo', 25.00,
         'transferidor', 4.20,
         'compasso', 9.99,
         'mochila', 120.32,
         'canetas', 22.30,
         'livros', 34.90)

print('-' * 55)
print('{:^55}'.format('LISTAGEM DE PRECO'))
print('-' * 55)
for c in range(0, len(produ)):
    if c % 2 == 0:
        print(f'{produ[c]:.<45}', end=' ')
    else:
        print(f'R${produ[c]:>7.2f}')
print('-' * 55)