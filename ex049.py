numerador = int(input("Digite o valor que ira ser o multiplicador: "))

for c in range(0, 10+1):
    print("{} x {:2} = {}".format(numerador, c, numerador * c))