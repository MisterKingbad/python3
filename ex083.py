exp = str(input('Digite a expressao: '))
pilhs = []
for simb in exp:
    if simb == '(':
        pilhs.append('(')
    elif simb == ')':
        if len(pilhs) > 0:
            pilhs.pop()
        else:
            pilhs.append(')')
            break
if len(pilhs)== 0:
    print('sua expressao esta valida!!')
else:
    print('sua expressao esta invalida!')