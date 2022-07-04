# cotaçao
quantos = (input("Digite:"))
money = 125.32

if quantos == "Quantos eu tenho?":
    print("Você tem {} reais".format(money))
else:
    exit()

resp = input("Fazer cotação? S/N: ")
cot_dol = 5.21


if resp == "S":
    print("Você terá em Dólar {:.2f}".format(money / cot_dol))
else:
    exit("FIM")

