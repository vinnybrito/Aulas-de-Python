# 26. Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja 
# negativo, imprimindo o resultado.

n = int(input('Digite um valor qualquer: '))

r = n % 2

if (r == 1):
    r = n * 3
    print('O valor digitado é um número negativo. O triplo de tal valor corresponde á', r)
else:
    r = n * 2
    print('O valor digitado é um número positivo. O dobro de tal valor corresponde á', r)
