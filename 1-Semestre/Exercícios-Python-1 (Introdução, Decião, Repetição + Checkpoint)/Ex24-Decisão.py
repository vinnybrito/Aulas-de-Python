# 24. Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso 
# sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

name = input("Insira o seu nome: ")

sex = input("Insira o seu sexo (Masculino = m / Feminino= f): ")

ec = input(" 1- Solteiro(a) \n 2- Casado(a) \n 3- Viuvo(a) \n Insira o seu estado civil: ")

if (sex == "f") and (ec == "2"):
    input("Por favor, insira há quanto tempo você está casada: ")
    print(f"Muito obrigado {name}!")
else:
    print(f"Muito obrigado {name}!")
