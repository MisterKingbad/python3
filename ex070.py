preco_count_mais_de_mil = soma_count_preco = preco_menor = cont = 0
barato = ''
print('=====MERCADIN BARATAO=====')
while True:
    nome_p = str(input('Nome do produto: '))
    preco = float(input('preco: R$'))
    cont += 1
    soma_count_preco += preco
    # IFS
    if preco > 1000:
        preco_count_mais_de_mil += 1
    if cont == 1 or preco < preco_menor:
        preco_menor = preco
        barato = nome_p
    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUER CONTINUAR? [S/N]:')).upper().strip()[0]
    if resp == 'N':
        break

print(f'O total dos produtos comprados foram de  R${soma_count_preco:.2f}')
print(f'Tem {preco_count_mais_de_mil} produtos que custam mais de R$1000')
print(f'O produto mais barato e "{barato}" com o preco de {preco_menor:.2f}')
