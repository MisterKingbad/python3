from random import shuffle
n1 = str(input("1 aluno"))
n2 = str(input("2 aluno"))
n3 = str(input("3 aluno"))
n4 = str(input("4 aluno"))
listas = [n1, n2, n3, n4]
shuffle(listas)
print("a ordem de apresentação sera:")
print(listas)