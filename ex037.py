print("==" * 20)
print("\033[1;31m          base de conversor\033[m")
print("==" * 20)
valores = int(input("Digite um valor:"))
escolha = str(input("\033[1;37mEscolha a base de conversão expl: BIN,OCT,HEX\033[m:")).strip().upper()

binario = valores
octal = valores
hexadecimal = valores
if escolha == "BIN":
    print(bin(valores)[2:])
elif escolha == "OCT":
    print(oct(valores)[2:])
elif escolha == "HEX":
    print(hex(valores)[2:])