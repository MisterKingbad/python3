# se o carro ultrapassar os 80km/h ele sera multado e a multa sera por cada Km rodado acima do limite permitido.
from time import sleep
km = float(input("\033[1;4;31mQuantos km/h o carro passou?\033[m"))
print("\033[1;32mPROCESSANDO....")
sleep(2)
if km > 80:
    custo = (km-80)*7
    print(f"\033[1;30;41mVOCÊ FOI MULTADO!! VOCÊ TERÁ QUE PAGAR R${custo}!\033[m")
else:
    print("\033[1;30;42mSe cuide e dirija com segurança!\033[m")