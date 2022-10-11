# 51- Armazenar dez números na memória do computador. Exibir os valores na ordem inversa à da digitação.

n = [] #Declarar um Array;

for i in range(0, 4, 1): #Enquanto "i" estiver no intervalo de 0 á 10...
    n.append(int(input("Digite um valor: ")))
    #O código vai se repitir 10 vezes e armazenar o valor digitado no Array;

for i in range(3, -1, -1):
    print(n[i])
