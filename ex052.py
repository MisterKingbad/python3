n = int(input("Digite um valor para ver se ela é um numero primo:"))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;32m{}\033[m'.format(c), end=' ')
        tot += 1
    else:
        print("\033[1;31m{}\033[m".format(c), end=' ')
print("\no numero {} foi divisivel {} vezes".format(n, tot))
if tot == 2:
    print("Por isso ele é PRIMO!")
else:
    print("por isso ele NÃO É PRIMO!")
