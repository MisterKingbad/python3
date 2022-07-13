'''a = int(input("Primeiro termo:"))
r = int(input("Razao:"))
dec = a + (10 - 1) * r

c = a
while c < dec + r:
    print('{}'.format(c), end='-> ')
    c = c + r
print("fim")'''

primeiro = int(input('primeiro'))
razao = int(input('Razao'))
termo = primeiro
count = 1
while count <= 10:
    print('{}'.format(count), end='')
    termo = termo + razao
    count = count + 1
print('fim')