s = 0
p = 0
p2 = 0
i = 1

n = int(input('Digite um valor positivo, menor que vinte: '))
    
while (n < 0) or (n > 20):
    n = int(input('O valor precisa ser positivo e menor que 20.\nDigite novamente: '))


while(i <= n):
    v = int(input('Digite os valores: '))

    if (i == 1):
        ma = v
    elif(v > ma):
        ma = v

    if (i == 1):
        me = v
    elif(v < me):
        me = v

    if(v > 0):
        p = p + 1
        x = (p * 100) / n

    if(v < 0):
        p2 = p2 + 1
    x2 = (p2 * 100) / n

    i = i + 1

    s = s + v

md = s / n
 
print ('1- O maior valor é: ', ma)
print ('2- O menor valor é: ', me)
print ('3- A soma dos valores é: ', s)
print ('4- A média aritmética dos valores é: ', md)
print (f'5- A porcentagem dos valores que são positivos é: {x}%')
print (f'6- A porcentagem dos valores que são negativos é: {x2}%')