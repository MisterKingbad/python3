matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'DIGITE UM VALOR EM [{l},{c}]: '))
print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end="")
    print()