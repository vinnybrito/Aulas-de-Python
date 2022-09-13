s = 0
p = 0
p2 = 0

n = int(input('Digite um valor positivo, menor que vinte: '))
    
while (n < 0) or (n > 20):
    n = int(input('O valor precisa ser positivo e menor que 20.\nDigite novamente: '))


for i in range(1, n+1, 1):
    v = int(input('Digite os valores: '))

    #Exibir o maior deles.
    if (i == 1):
        ma = v
    elif(n > ma):
        ma = v

    #Exibir o menor deles.
    if (i == 1):
        me = v
    elif(v < me):
        me = v

    #Porcentagem dos valores positivos.
    if(v > 0):
        p = p + 1
        x = (p * 100) / n

    #Porcentagem dos valores negativos.
    if(v < 0):
        p2 = p2 + 1
    x2 = (p2 * 100) / n

    #A soma de todos os valores.
    s = s + v

#A média aritmética dos valores.
md = s / n
 
print ('1- O maior valor é: ', ma)
print ('2- O menor valor é: ', me)
print ('3- A soma dos valores é: ', s)
print ('4- A média aritmética dos valores é: ', md)
print (f'5- A porcentagem dos valores que são positivos é: {x}%')
print (f'6- A porcentagem dos valores que são negativos é: {x2}%')