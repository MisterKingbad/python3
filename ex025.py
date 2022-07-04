# nome tem silva e é valido nao importa onde esteja começo, meio, fim, tanto faz.
nome: str = input("Digite seu nome: ").strip()
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))