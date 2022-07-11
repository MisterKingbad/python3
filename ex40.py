# medias
not1 = float(input('informe a primeira nota:'))
not2 = float(input('informe a segunda nota:'))

media = (not1 + not2) / 2

if media >= 7.0:
    print('\033[1;30;42mAPROVADO\033[m')
elif 7 > media >= 5.0:
    print('\033[1;32mRECUPERAÇÃO\033[m')
else:
    print("\033[1;30;41mREPROVADO\033[m")