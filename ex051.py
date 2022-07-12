a = int(input("Primero termo: "))
r = int(input("Razao: "))
dec = a + (10 - 1) * r
for c in range(a, dec + r, r):
    print('{}'.format(c), end='-> ')
print("fim")
