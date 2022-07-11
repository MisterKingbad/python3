import datetime
idade = int(input('Em que ano você nasceu?\033[37mex:2022\033[m'))

ano = datetime.date.today().year
result = ano - idade
if result == 18:
    print('\033[1;30;42mJÁ TA NA HORA DE SE ALISTAR!\033[m')
elif result < 18:
    result = 18-result
    print(f'\033[1;32mVocê é novo, falta {result} ano para se alistar. Seu alistamento sera em {ano + result} \033[m')

else:
    result = result - 18
    print(f'\033[1;30;41mJÁ PASSOU {result} ANOS D0 TEMPO DO ALISTAMENTO DESDE {ano - result}!\033[m')
