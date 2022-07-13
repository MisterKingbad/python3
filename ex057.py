sx = str(input("DIGITE O SEXO M/F:")).strip().upper()[0]
while sx not in 'MmFf':
    sx = str(input("Dados invalidos. TENTE NOVAMENTE")).strip().upper()
print(' VOCE ESCOLHEU "{}"'.format(sx))
