peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input('Qual é a sua altura? (M) '))
imc = peso / (altura ** 2)
print("O imc dessa pessoas é de {:.1f}".format(imc))
if imc < 18.5:
    print("\033[4;32mvoce esta abaixo do peso ideial. TOMA WHEY")

elif 18.5 <= imc < 25:
    print('\033[32mVocê esta no peso ideal')

elif 25 <= imc < 30:
    print('\033[31mVOCÊ ESTA EM SOBREPESO!\033[m')

elif 30 <= imc < 40:
    print('\033[4;31mVOCÊ ESTA EM OBESIDADE!\033[m')

else:
    print('\033[1;30;41mVOCÊ ESTA EM OBESIDADE MORBIDA!!\033[m')

