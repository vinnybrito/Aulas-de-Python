# 32. Entrar com dois valores via teclado, onde o segundo deverá ser maior que o 
# primeiro. Caso contrário solicitar novamente apenas o segundo valor.

v1 = int(input('Digite o primeiro valor: '))

v2 = int(input('Digite um valor que seja maior que o primeiro: '))

while (v2 < v1):
    v2 = int(input('O segundo valor precisar se maior que o primeiro.\nDigite novamente: '))
print('Obrigado!')
