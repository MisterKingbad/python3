import datetime

idadeatle = int(input('Qual é o ano que o atleta nasceu?'))

anoatual = datetime.date.today().year

result = anoatual - idadeatle
print("o atleta tem {} anos".format(result))


if result <= 9:
    print('Um Atleta mirin')
elif result <= 14:
    print('Um atleta infantil')
elif result <= 19:
    print('Um atleta junior')
elif result <= 20:
    print('Um atleta sênior')
else:
    print('Um atleta Master')