import os
import pandas as pd

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
diretorio_data = os.path.join(diretorio_atual, 'datasets')

# lista todos os arquivos na pasta "data"
arquivos = os.listdir(diretorio_data)

for arquivo in arquivos:
    if arquivo.endswith('.xlsx'):
        caminho_arquivo = os.path.join(diretorio_data, arquivo)
        df = pd.read_excel(caminho_arquivo)
        
        # remove 'sex', 'race' e 'housing'
        colunas_a_remover = ['Sex', 'Race', 'Housing']
        df = df.drop(columns=colunas_a_remover, errors='ignore')
        
        # salva o conjunto de dados atualizado no mesmo arquivo
        df.to_excel(caminho_arquivo, index=False)
