frase = str(input("Escreva qualquer frase: ")).strip().upper()
frase = frase.split()
frase = ''.join(frase)
inve = ''
for l in range(len(frase) -1,-1, -1):
    inve += frase[l]
if inve == frase:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")