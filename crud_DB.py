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
    inst_cadastro = connection.cursor()
    inst_consulta = connection.cursor()
    inst_alteracao = connection.cursor()
    onst_exclusao = connection.cursor()
    
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
    
else:
    print("Erro ao mexer na tabela!!!")