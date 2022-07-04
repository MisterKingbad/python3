# mostrar o primeiro nome e o ultimo
nome: str = input('Digite seu nome: ').strip()
primeiro_nome = nome.split()
primeiro_nome = primeiro_nome[0]
print("O seu primeiro nome é {}".format(primeiro_nome))
ultimo_nome = nome.split()
ultimo_nome = ultimo_nome[len(ultimo_nome)-1]
print("o seu ultimo nome é {}".format(ultimo_nome))
