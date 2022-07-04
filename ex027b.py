# ler so o primeiro nome e o ultimo
nome = str(input("Digite seu nome: "))
n = nome.split()
'''print("Seu primeiro nome é: {}".format(n[0]))
print("seu ultimo nome é: {}".format(n[len(n)-1]))'''

print(f"O primeiro nome é '{n[0]}' e o ultimo nome é '{n[-1]}'")