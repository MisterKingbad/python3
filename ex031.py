# cobrar passage por 200km
passagem = float(input("\033[1;30;44mQual vai ser a distancia da sua viagem?:\033[m"))

if passagem <= 200:
    pagar = passagem * 0.50
    print(f"\033[1;30;42mBoa viagem. Esse é o valor que se deve pagar R${pagar}.")
else:
    pagar = passagem * 0.45
    print(f"\033[1;30;41mSua viagem é longa. Esse é o valor que se deve pagar R${pagar}.")
