# 14- Entrar com o peso e a altura de uma determinada pessoa. Após a digitação, 
# exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

p = float(input('Digite o seu peso (em kg): '))

a = float(input('Digite a sua altura em (m): '))

imc = p / (a * a)

if (imc < 20):
    print('Abaixo do peso.')
elif(imc < 25):
    print('Peso ideal.')
else:
    print('Acima do peso.')
