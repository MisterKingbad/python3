

c = 1
while c != 10:
    n1 = int(input("Coloque o primeiro valor: "))
    n2 = int(input("Coloque o segundo valor: "))
    print('''O QUE DESEJA FAZER
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos numeros
    [5]Sair do programa''')
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print("A soma entre {} e {} é {}".format(n1, n2, n1 + n2))
    if opcao == 2:
        print("Multiplicação: {} X {} = {}".format(n1, n2, n1 * n2))
    if opcao == 3:
        #verif numero menor
        menor = n1
        if n2 < n1:
            menor = n2
        print("o menor é {}".format(menor))

        #verif numero maior
        maior = n1
        if n2 > n1:
            maior = n2
        print("O MAIOR É {}".format(maior))
    if opcao == 4:
        print('')
    if opcao == 5:
        break
print("FIM")