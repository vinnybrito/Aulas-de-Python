# 12- Calcular e exibir a área de um retângulo, a partir dos valores da base e altura 
# que serão digitados. Se a área for maior que 100, exibir a mensagem “Terreno 
# grande”, caso contrário, exibir a mensagem “Terreno pequeno”.

b = int(input('Digite o valor da base do retângulo: '))

h = int(input('Digite o valor da altura do retângulo: '))

a = b * h

if (a > 100):
    print('Terreno grande!')
else:
    print('Terreno pequeno!')
    