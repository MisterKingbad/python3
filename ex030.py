# par ou impar?
num = int(input("Digite um valor: "))

if num % 2 == 0:
    print(f"\033[1;4;32mO numero {num} é par!")
else:
    print(f"\033[1;4;31mO numero {num} é impar!")
