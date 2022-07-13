nint = count = soma = 0
nint = int(input('valor: '))
while nint != 999:
    soma += nint
    count += 1
    nint = int(input('valor: '))
print('foram digitados {} e a soma dos numeros digitados eh {}'.format(count, soma))
print('FIM')