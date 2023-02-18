# 33- Entrar via teclado com o sexo de determinado usuário, aceitar somente “F” ou 
# “M” como respostas válidas.

sex = input('Insira o seu sexo (Masculino = m / Feminino = f): ')

while (sex != "m") and (sex != "f"):
    sex = input('Sexo invalido. Insira novamente: ')
print('Obrigado!')
