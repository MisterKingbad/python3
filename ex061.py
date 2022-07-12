a = int(input("Primeiro termo:"))
r = int(input("Razao:"))
dec = a + (10 - 1) * r

c = a
while c < dec + r:
    print('{}'.format(c), end='-> ')
    c = a + r
print("fim")
