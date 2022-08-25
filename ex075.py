num = (int(input('valor1: ')), int(input('valor2: ')), int(input('valor3: ')), int(input('valor4: ')))

print(f'Voce digitou os valores {num}')
print(f'o valor 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'o primeiro numero 3 digitado esta na posicao {num.index(3) + 1}o.')
else:
    print('O numero 3 nao foi digitado')
print('os valores pares digitados foram', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
