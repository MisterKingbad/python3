# Aluguel de carro

dias = int(input("Quantos dias usou o carro? "))
km = float(input("quantos Km percorreu? "))
pagar = (dias * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(pagar))
