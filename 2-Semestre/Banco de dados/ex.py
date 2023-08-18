import cx_Oracle

# Cria String de conexão com informações do Host, Porta e SID
dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')

# Estabelece conexão com o BD
conn = cx_Oracle.connect(user='rm97473', password='240700', dsn=dsn)

# Abrir um cursor para executar comandos SQL
cursor = conn.cursor()

# Inserindo valores na tabela
cursor.execute("INSERT INTO TB_USUARIO (ID, NOME) VALUES (:valor1, :valor2)", valor1=1, valor2='Joseffe')
conn.commit()

print('Registro incluído com sucesso!')

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
