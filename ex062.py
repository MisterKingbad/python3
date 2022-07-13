print('----- PA -----')
'''resp = 'S'''
'''while resp == 'S':'''
'''resp = str(input("\n\033[1mQuer continuar? S/N\033[m")).strip().upper()'''
p = int(input("Primeiro termo: "))
r = int(input("Razao"))
termo = p
c = 1
tot = 0
mais = 10
while mais != 0:
    tot = tot + mais
    while c <= tot:
        print('{}'.format(termo), end=" -> ")
        termo += r
        c += 1
    print('pausa')
    mais = int(input("quer mostrar mais quando termos?"))
print("fim. termos {}".format(tot))


