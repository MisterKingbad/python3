# q mostre o primeiro e ultimo 'a'
frase = str(input("Digite qualquer coisa: ")).strip().upper()
cont_a = frase.count("A")
print("A letra 'a' aparece {} vezes".format(cont_a))
prim_a = frase.find("A")+1
print("A primera letra 'a' esta na posição {}".format(prim_a))
ult_a = frase.rfind("A")+1
print("A ultima letra 'a' aparece na posição {}".format(ult_a))
