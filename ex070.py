preco = preco_maior = preco_count_mais_de_mil = soma_count_preco = preco_menor= 0
resp = 'S'
print('=====MERCADIN BARATAO=====')
while resp in 'Ss':
    nome_p = str(input('Nome do produto: '))
    preco = float(input('Valor: '))
    soma_count_preco += preco
    # IFS
    if preco > 1000:
        preco_count_mais_de_mil += 1

    resp = str(input('QUER CONTINUAR? [S/N]: ')).upper().strip()[0]

print(f'O total dos produtos comprados foram de  R${soma_count_preco}')
print(f'Tem {preco_count_mais_de_mil} produtos que custam mais de R$1000')
print(f'O produto mais barato e {nome_p} com o preco de {preco_menor}')


