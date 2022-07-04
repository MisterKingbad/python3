'''from math import pow, sqrt
v1 = float(input("Informe o valor do primeiro cateto: "))
v2 = float(input("Informe o valor do segundo cateto: "))
a = pow(v1, 2)
b = pow(v2, 2)
print("a exponenciação de {} e {} é: {} e {}".format(v1, v2, a, b))
x = a + b
print("A soma de {} e {} é: {}.".format(a, b, x))
hip = x
hip = sqrt(hip)
print("A raiz de {} é: hip {:.2f}.".format(x, hip)'''
from math import hypot

co = float(input("comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adjacente: "))
hi = hypot(co, ca)
print("a hipotenusa vai medir {:.2f}".format(hi))
