
while True:
    print('='*30)
    tb = int(input("QUER VER A TABUADA DE QUAL VALOR?:"))
    print('='*30)
    if tb < 0:
        break
    for c in range (1,11):
        print(f'{tb} x {c} = {tb*c}')
print('Programa encerrada')



