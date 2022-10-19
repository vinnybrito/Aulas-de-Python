# 10 Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.

v1 = int(input('Digite o primeiro valor: '))

v2 = int(input('Digite o segundo valor: '))

if (v1 > v2):
    print('O primeiro valor é o maior.')
elif (v1 == v2):
    print('Os valores são idênticos.')
else:
    print('O segundo valor é o maior.')
    