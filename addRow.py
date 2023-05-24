import os
import csv

diretorio = '/media/joao/F08CC4158CC3D46E/teste1/SQL'

i = 0
for nome_arquivo in os.listdir(diretorio):
    i = i + 1
    if nome_arquivo.endswith('.csv'):
        arquivo_csv = os.path.join(diretorio, nome_arquivo)
        
        with open(arquivo_csv, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            dados = list(leitor_csv)
            
        nova_linha = [
        'id_financeiro',
        'id_contratante',
        'data',
        'valor',
        'forma',
        'de_para',
        'id_centro_custo',
        'bandeira',
        'banco',
        'agencia',
        'conta',
        'numero',
        'bompara',
        'id_contratante_usuario',
        'auditoria',
        'baixa',
        'id_agenda',
        'nf',
        'id_conta',
        'justificativa',
        'cd_recorrencia',
        'id_procedimento',
        'id_paciente',
        'id_fluxo_movimentacao']
        dados.insert(0, nova_linha)
        
        with open(arquivo_csv, 'w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerows(dados)
            print(f'Arquivo {i} processado.')
