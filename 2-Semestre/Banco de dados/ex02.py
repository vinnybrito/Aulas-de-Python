saldo = 10

valor = int(input('Digite o pagamento: '))

resultado = saldo - valor

if (valor <= saldo):
    print("Compra aprovada")
    print(resultado)
else:
    print("Compra negada!")
    print(resultado)