# 31. Criar uma rotina de entrada que aceite somente um valor positivo.

v1 = int(input('Digite um valor positivo: '))

while (v1 < 0):
    v1 = int(input('Valores negativos não são permitidos.\nDigite novamente: '))
print('Obrigado!')
