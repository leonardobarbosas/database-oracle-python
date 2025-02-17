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
    
nome_cachorro = input("Digite o nome do cachorro: ")
tipo_cachorro = input("Digite o tipo do cachorro: ")
idade_cachorro = int(input("Digite a idade do cachorro: "))

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
    print("INSERINDO EM UMA TABELA NO DB ORACLE\n")
    DB_insert = f'''insert into testepetshop(tipo_pet, nome_pet, idade) values('{tipo_cachorro}', '{nome_cachorro}', {idade_cachorro})'''
    print(DB_insert)
        
    #executa e grava o registro da tabela
    instrucao_1.execute(DB_insert)
    connection.commit()
    
    print("Valor inserido com sucesso!!!")

    connection.close()
else:
    print("Erro ao inserir na tabela!!!")