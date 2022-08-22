idade = sexo = c_hom = idade_mulher = idade_homen = c_mul = total = count_h = count_m = 0
homen = 'M'
mulher = 'F'
resp = ' '
while True:
    idade = int(input('Digite idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual e o sexo da pessoa?[M/F]: ')).upper().strip()[0]

    if sexo in homen:
        print(homen)
        c_hom += 1
        idade_homen = idade
        if idade_homen >= 18:
            count_h += 1

    else:
        print(mulher)
        idade_mulher = idade
        if idade_mulher < 20:
            c_mul += 1
        if idade_mulher >= 18:
            count_m += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('DESEJA CONTINUAR?[S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Tem {count_h + count_m} pessoas maior de 18.')
print(f'foram cadastrado {c_hom} homens.')
print(f'foram cadastrado {c_mul} mulheres com menos de 20 anos.')
