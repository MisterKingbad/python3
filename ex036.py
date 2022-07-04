valorcasa = float(input("\033[1;32mQual é o valor da casa?:\033[m"))
salario = float(input("\033[1;32mQuanto você ganha?:\033[m"))
anospagar = float(input("\033[1;32mEm quantos você ira pagar a casa?:\033[m"))

prestacao = valorcasa / anospagar
print("Você tera que pagar por mês?:R${}".format(prestacao))

prestacao = prestacao + (prestacao * 30 / 100)

if prestacao > salario:
    print("\033[1;30;41mINFELIZMENTE VOCÊ NÃO TEM CONDIÇÕES PARA FINANCIAR ESSA CASA.\033[M ")
else:
    print("\033[1;30;42Parabens! Você pode finamciar essa casa.\033[m")