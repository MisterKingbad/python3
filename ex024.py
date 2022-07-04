# somente no começo a palavra santos
cidade: str = input("Digite o nome da sua cidade: ").strip()
cidade = cidade.split()
cidade = cidade[0]
print("SANTO" in cidade.upper())
