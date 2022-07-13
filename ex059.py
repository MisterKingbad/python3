from time import sleep
n1 = int(input("Coloque o primeiro valor: "))

n2 = int(input("Coloque o segundo valor: "))

opcao = 0
while opcao != 5:
    print('''O QUE DESEJA FAZER
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos numeros
    [5]Sair do programa''')
    opcao = int(input("Escolha a opção: "))
    if opcao == 1:
        print("A soma entre {} e {} é {}".format(n1, n2, n1 + n2))
    elif opcao == 2:
        print("Multiplicação: {} X {} = {}".format(n1, n2, n1 * n2))
    elif opcao == 3:
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
    elif opcao == 4:
        print('informe os numeros novamente:')
        n1 = int(input('Coloque o primeiro valor'))
        n2 = int(input('Coloque o segundo valor:'))
    elif opcao == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('opcao invalida.')
    print('===========================================')
    sleep(1.5)
print("FIM")