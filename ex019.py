'''import random
sorteia = random.randint(1, 4)

if sorteia == 1:
    print("Eduu")
else:
    if sorteia == 2:
        print("Lisa")
    else:
        if sorteia == 3:
            print("Gustavo")
        else:
            if sorteia == 4:
                print("Mari")'''

import random
al1 = input("primeiro aluno:")
al2 = input("segundo aluno:")
al3 = input("terceiro aluno:")
al4 = input("quarto aluno:")
lista = [al1, al2, al3, al4]
escolha = random.choice(lista)
print("o aluno escolhido foi {}".format(escolha))