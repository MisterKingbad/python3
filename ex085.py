lista = [[], []]
valor = 0
for c in range(0, 7):
    valor = (int(input(f'digite o {c+1}o. valor: ')))
    if valor % 2 == 0:
        #Lista[0] par
        lista[0].append(valor)
    elif valor % 2 == 1:
        #Lista[1] Impar
        lista[1].append(valor)
print(f'Todos os valores sao: {lista}')
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')
