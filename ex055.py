maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("QUAL É O PESO DA {}A PESSOA:".format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("O maior peso lido é {}Kg".format(maior))
print('O manor peso lido é {}Kg'.format(menor))