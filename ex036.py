valorcasa = float(input("\033[1;32mQual é o valor da casa?:\033[m"))
salario = float(input("\033[1;32mQuanto você ganha?:\033[m"))
anospagar = int(input("\033[1;32mEm quantos anos você ira pagar a casa?:\033[m"))
prestacao = valorcasa / (anospagar * 12)
minimo = salario * 30 / 100
print("para pagar uma casa de R${} em {} anos".format(valorcasa, anospagar), end=' ')
print('a prestação sera de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print("\033[1;30;42mParabens! Você pode financiar essa casa.\033[m")
else:
    print("\033[1;30;41mINFELIZMENTE VOCÊ NÃO TEM CONDIÇÕES PARA FINANCIAR ESSA CASA.\033[M ")
