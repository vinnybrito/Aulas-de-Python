# 18- Criar um programa para analisar a velocidade de um automóvel. Solicitar via 
# teclado os valores da aceleração (a em m/s2), velocidade inicial (v0 em m/s) e o 
# tempo de percurso (t em s).Calcular e exibir avelocidade final do automóvelem km/h. 
# E exibir mensagem de acordo com a tabela abaixo:
# Fórmula para o cálculo da velocidade em m/s: V = v0 + a. t

a = float(input('Digite o valor da aceleração (em m/s2): '))

v0 = float(input('Digite o valor da velocidade inicial (em m/s): '))

t = float(input('Digite o valor do tempo de percurso (t em s): '))

v = v0 + (a * t)

if (v <=40):
    print('Veículo muito lento, a velocidade é:', v)
elif (v <= 60):
    print('Velocidade permitida, a velocidade é:', v)
elif (v <= 80):
    print('Velocidade de cruzeiro, a velocidade é:', v)
elif (v <= 120):
    print('Veículo rápido, a velocidade é:', v)
else:
    print('Veículo muito rápido, a velocidade é:', v)
