# maior e menor
n1 = int(input("\033[1;31mDigite um numero: "))
n2 = int(input("\033[1;31mDigite o segundo numero: "))
n3 = int(input("\033[1;31mDigite o terceiro numero:\033[m"))
# Verificando numero menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("\033[4;1;32mO menor é {}".format(menor))

# verificando numero maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"\033[4;1;34mO maior é {maior}")
