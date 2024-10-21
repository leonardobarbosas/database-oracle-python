import cx_Oracle
from user_data import user_, pass_
import os
import pandas as pd


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

    # Usará todo o tempo e fecha com o fechamento da aplicação
    # Efetua a conexão com o Usuário
    # Deve ser fechada ao sair do programa connection.close()
    connection = cx_Oracle.connect(
        user=user_, 
        password=pass_,
        dsn=dsn_string,
        encoding="UTF-8")

    # Cria as instruções para cada módulo
    inst_cadastro = connection.cursor() #Create
    inst_consulta = connection.cursor() #Read
    inst_alteracao = connection.cursor() #Update
    inst_exclusao = connection.cursor() #Delete

except Exception as e:
# Informa o erro
    print("Erro: ", e)
    # Flag para não executar a Aplicação
    conexao = False

else:
    # Flag para executar a Aplicação
    conexao = True
    print('Conectado com sucesso!!!')


margem = "  "


# Enquanto o flag conexao estiver apontado com True a aplicação é executada
while conexao:
    
    # Apresenta o menu
    print("---- CRUD - PETSHOP ----")
    print("""
    1 - Cadastrar Pet
    2 - Listar Pets
    3 - Alterar Pet
    4 - Excluir Pet
    5 - EXCLUIR TODOS OS PETS
    6 - SAIR
    """)

    try:
        # Captura a escolha do usuário
        escolha = int(input(margem + "Escolha -> "))
    except Exception as err:
        print('\nVocê selecionou uma opção inválida! Digite um número entre 1 e 6...')
    else:
        print('\nCarregando opções...')


    # VERIFICA QUAL A ESCOLHA DO USUÁRIO
    match escolha:
    # CADASTRAR UM PET
        case 1:
            try:
                print("----- CADASTRAR PET -----\n")
                
                # Recebe os valores para cadastro
                tipo = input(margem + "Digite o tipo....: ")
                nome = input(margem + "Digite o nome....: ")

                idade = int(input(margem + "Digite a idade...: "))

                # Monta a instrução SQL de cadastro em uma string
                # Usando f....string {valores} é mais rápido
                cadastro = f"INSERT INTO petshop (tipo_pet, nome_pet, idade) VALUES ('{tipo}', '{nome}',{idade})"

                # Executa e grava o Registro na Tabela
                inst_cadastro.execute(cadastro)
                connection.commit()

            except ValueError:
                print("Digite um número na idade!")

            except Exception as err:
                print(f"Erro na transação do BD. Err:{err}")

            else:
                print("\nDados GRAVADOS")
                input("Presione ENTER para continuar ...")
                
        case 2:

            os.system('cls')
            print("----- LISTANDO PETs -----\n")
            lista_pets = [] #aqui vamos armazenar os dados

            # Executa a leitura da Tabela
            consulta = "SELECT * FROM petshop"
            inst_consulta.execute(consulta)

            # Aqui coletamos a consulta
            dados = inst_consulta.fetchall()

            for linha in dados:
                lista_pets.append(linha)

            lista_pets = sorted(lista_pets)

            colunas = ['Id', 'Tipo', 'Nome', 'Idade']
            # Aqui o nosso Dataframe!!!!!
            df_pets = pd.DataFrame.from_records(lista_pets, columns=colunas, index='Id')


            print('Listando os pets cadastrados...\n')
            print(df_pets)
            _ = input("\nPresione ENTER para continuar ...")

        case 3:
            os.system('cls')
            print("----- ALTERANDO CADASTRO DE PET -----\n")

            pet_id = int(input('Digite o Id do pet cujo cadastro quer alterar: '))

            lista_pet = [] #aqui vamos armazenar os dados

            # Executa a leitura da Tabela
            consulta = f"SELECT * FROM petshop WHERE Id = {pet_id}"
            inst_consulta.execute(consulta)
            dado = inst_consulta.fetchall()

            lista_pet.append(dado)

            if len(lista_pet) == 0:
                print(f"Não há pet com o Id = {pet_id}")
                _ = input("\nPresione ENTER para continuar ...")
            else:
                tipo_alt = input("Digite o novo tipo para o pet: ")
                nome_alt = input("Digite o novo nome para o pet: ")
                idade_alt = int(input("Digite a nova idade para o pet: "))

                alteracao = f"UPDATE petshop SET tipo_pet='{tipo_alt}', nome_pet='{nome_alt}', idade='{idade_alt}' WHERE id='{pet_id}'"
                inst_alteracao.execute(alteracao)
                connection.commit()
            
                print('Alteração executada com sucesso...\n')
                _ = input("\nPresione ENTER para continuar ...")
                
        case 4:
            os.system('cls')
            print("----- EXCLUINDO CADASTRO DE PET -----\n")
            
            pet_id = int(input('Digite o Id do pet cujo cadastro quer excluir: '))
            
            lista_pet = [] #aqui vamos armazenar os dados
            
            # Executa a leitura da Tabela
            consulta = f"SELECT * FROM petshop WHERE Id = {pet_id}"
            inst_consulta.execute(consulta)
            dado = inst_consulta.fetchall()
            
            lista_pet.append(dado)
            
            if len(lista_pet) == 0:
                print(f"Não há pet com o Id = {pet_id}")
                _ = input("\nPresione ENTER para continuar ...")
            else:
                exclusao = f"DELETE FROM petshop WHERE id = {pet_id}"
                inst_exclusao.execute(exclusao)
                connection.commit()
                
                print('Exclusão executada com sucesso...\n')
                _ = input("\nPresione ENTER para continuar ...")
        case 5:
            os.system('cls')
            print("----- EXCLUINDO TODOS OS PETS -----\n")
            
            exclusao = "DELETE FROM petshop"            
            inst_exclusao.execute(exclusao)
            connection.commit()
            
            data_reset_ids = "ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1))"
            inst_exclusao.execute(data_reset_ids)
            connection.commit()
            
            print('Exclusão executada com sucesso...\n')
            _ = input("\nPresione ENTER para continuar ...")
        case _:
            print('\nDigite uma opção válida...')
            input("\nPresione ENTER para continuar ...")
                