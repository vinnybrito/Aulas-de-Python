# 2- Crie um programa em Pyhton que permita consultar Devs no GitHub. O programa 
# deve consumir a API do GitHub (Exemplo: https://api.github.com/users/joseffe10), 
# permitindo o usuário digitar algum login do GitHub e após isso retornar as 
# informações.

import requests

print('<<----PERFIL GITHUB---->>')

github = input("\nDigite o login do GitHub: ")
url = f"https://api.github.com/users/{github}"

response = requests.get(url)

if response.status_code == 200:
    dados = response.json() 
      
    print(f"\nNome: {dados['name']} | Repositórios: {dados['public_repos']} | Seguidores: {dados['followers']}")
else:
    print("Perfil não encontrado.")