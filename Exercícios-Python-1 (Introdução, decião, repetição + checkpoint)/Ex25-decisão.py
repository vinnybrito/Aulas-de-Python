# 25. Faça um algoritmo para receber um número qualquer e informar na tela se é par 
# ou ímpar. Utilize o operador %

n = int(input("Digite um valor qualquer: "))

r = n % 2

if (r == 0) :
    print("É um número par.")
else:
    print("É um número impar.")
