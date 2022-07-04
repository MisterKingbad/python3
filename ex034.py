salario: float = float(input("\033[1;4;33mQual é seu salario atual?R$:\033[m"))

if salario >= 1250:
    salario = salario + (salario * 10 / 100)
    print("\033[34mSeu novo salario atual sera \033[1;32mR${:.3f}".format(salario))
else:
    salario = salario + (salario * 15 / 100)
    print("\033[34mSeu novo salario atual sera \033[1;32mR${:.3f}".format(salario))