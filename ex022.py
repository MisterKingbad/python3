nome: str = input("Digite seu nome completo: ")
print("Seu nome escrito normalmente: {}".format(nome))
print("Seu nome em 'MAIÚSCULAS': {}".format(nome.upper()))
print("Seu nome em 'minúsculas': {}".format(nome.lower()))
divide = nome.split()
juncao = ''.join(divide)
print("Seu nome {} completo/inteiro tem {} letras no total sem contar os espaços.".format(nome, len(juncao)))
print(divide[0])
primeiro_nome = divide[0]
juncao = ''.join(primeiro_nome)

print("seu primeiro nome {} tem {} letras".format(primeiro_nome, len(juncao)))
