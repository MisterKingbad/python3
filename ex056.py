somaidd = 0
mediaidd = 0
maioriddhomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print("----- {}a PESSOA -----".format(p))
    nome_p = str(input("NOME: ")).strip()
    idade_p = int(input("IDADE: "))
    sexo_p = str(input("SEXO [M/F]: ")).strip()
    somaidd += idade_p
    if p == 1 and sexo_p in 'Mm':
        maioriddhomem = idade_p
        nomevelho = nome_p
    if sexo_p in 'Mm' and idade_p > maioriddhomem:
        maioriddhomem = idade_p
        nomevelho  = nome_p
    if sexo_p in 'Ff' and idade_p < 20:
        totmulher20 += 1

mediaidd = somaidd / 4
print('A media de idade do grupo é de {} anos'.format(mediaidd))
print('O homem mais velho tem {} anos e se chama {}'.format(maioriddhomem,nomevelho))
print('E apenas {} Mulheres com menos de 20 anos'.format(totmulher20))



