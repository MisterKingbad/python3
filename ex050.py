for c in range(6):
    n = int(input("Digite um valor: "))
    print(n % 2)
    if n % 2 == 0:
        print("O valor total somado por pares é {}".format(n+n))