preco = float(input('Preço das compras: '))
print('''FORMAS DE PAGAMENTOS
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á  vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input("Qual é a sua opção?"))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("sua compra sera parcelada em 2x de R${:.2f} sem juros".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input("Quantas parcelas?"))
    parcela = total / totparc
    print(" sua compra sera parcela em {}x de R${:.2f} com juros".format(totparc, parcela))
else:
    total = preco
    print("\033[31mOPÇÃO INVALIDA DE PAGAMENTO. TENTE NOVAMENTE!\033[m")
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))