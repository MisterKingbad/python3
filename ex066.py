num = count = s = 0
while True:
    num = int(input('Digite um valor: '))

    if num == 999:     # por causa do break ela nao eh contada.
        break
    s += num
    count += 1
print(f'FORAM DIGITADOS {count} NUMEROS E A SOMA DELAS SAO {s}.')