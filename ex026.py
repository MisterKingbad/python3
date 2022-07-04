escreva: str = input("Escreva qualquer frase: ").strip().upper()
contador_a = escreva.count("A")
print("A letra 'a' aparece {} vezes".format(contador_a))
primeiro_a = escreva.find("A")+1
print("A letra 'a' começa NA POSIÇÃO {}".format(primeiro_a))
ultimo_a = escreva.rfind("A")+1
print("A letra 'a' acaba na posição {}".format(ultimo_a))
