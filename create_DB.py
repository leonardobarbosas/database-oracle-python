import cx_Oracle

from user_data import user_, pass_

host = 'oracle.fiap.com.br'
porta = '1521'
SID = 'orcl'

try:
    cx_Oracle.init_oracle_client(lib_dir= r"C:\Program Files\instantclient_23_5")
except Exception as e:
    print("Erro na inicialização do 'client': ", e)
else:
    print('Inicializado com sucesso!!!')

try:
    # Conecta o servidor
    dsn_string = cx_Oracle.makedsn(
        host, 
        porta, 
        SID)

    # Efetua a conexão com o Usuário
    connection = cx_Oracle.connect(
        user=user_, 
        password=pass_,
        dsn=dsn_string,
        encoding="UTF-8")

    # Cria as instruções para cada módulo
    instrucao_1 = connection.cursor()

except Exception as e:
# Informa o erro
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False

else:
    # Flag para executar a Aplicação
    conexao = True
    print('Conectado com sucesso!!!')
    
if conexao:
    print("CADASTRANDO UMA TABELA NO DB ORACLE\n")
    DB_create = f'''create table testepetshop(
        id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        tipo_pet VARCHAR2(50),
        nome_pet VARCHAR2(50),
        idade INT
        )'''
        
    #executa e grava o registro da tabela
    instrucao_1.execute(DB_create)
    connection.close()
    print("Tabela criada com sucesso!!!")
else:
    print("Erro ao criar a tabela!!!")