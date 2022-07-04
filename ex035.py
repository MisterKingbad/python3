# analisar triangulo
r1 = float(input("Primeiro lado:"))
r2 = float(input("segundo lado: "))
r3 = float(input("terceiro lado: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("\033[1;32mPode se formar um triangulo!")
else:
    print("\033[1;30;41mNÃO PODE SE FORMAR UM TRIANGULO!")
