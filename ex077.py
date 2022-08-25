# vogais
palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGRAMADOR',
            'FUTURO')
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')