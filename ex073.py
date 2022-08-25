times = ('PALMEIRAS', 'FLUMINENSE', 'FLAMENGO', 'CORINTHIANS', 'INTERNACIONAL', 'ATHLETICO-PR', 'ATLÉTICO-MG', 'SANTOS',
         'AMÉRICA-MG', 'RED BULL BRAGANTINO', 'GOIÁS', 'SÃO PAULO', 'FORTALEZA', 'BOTAFOGO', 'CEARÁ', 'CUIABÁ',
         'AVAÍ', 'CORITIBA', 'ATLÉTICO-GO', 'JUVENTUDE')
print('-='*15)
print(f'Lista de times do Brasileirao: {times}')
cin_pri_lugar = times[:5]
print('-='*15)
print(f'Os 5 primeros colocados sao: {cin_pri_lugar}')
qua_ult_lugar = times[-4:]
print('-='*15)
print(f'Os 4 ultimos colocados sao: {qua_ult_lugar}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*15)
print(f'O santos esta na {times .index("SANTOS")+1}a posicao')
