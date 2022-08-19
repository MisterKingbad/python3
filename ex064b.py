num = soma = 0
while True:
    n = int(input('digite os valores:'))
    if n == 999:
        break
    soma += n
print(f'a soma dos valores digitados eh {soma}')