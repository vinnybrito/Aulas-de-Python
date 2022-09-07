
sex = input("Insira o seu sexo (Masculino = m / Feminino = f): ")

while (sex.upper != ("m")) and (sex.upper != ("f")):
    print("Sexo incorreto")
    sex = input("Insira o seu sexo novamente (Masculino = m / Feminino = f): ")

print("Obrigado")