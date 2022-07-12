from time import sleep
n = int(input("ponha um numero para ver o seu fatorial: "))
c: int = n
while c > 0:
    sleep(0)
    print(c)
    c -= 1
    n = n * c
    print("o seu fatorial é {}".format(n))