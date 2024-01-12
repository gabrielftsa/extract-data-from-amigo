import pandas as pd
from FormatConverter import FormatConverter

# Caminho do arquivo CSV
caminho_arquivo_csv = r"C:\Users\User\Desktop\ResumoCompletoCSV.csv"

# Lê o arquivo CSV para um DataFrame
dataframe_csv = pd.read_csv(caminho_arquivo_csv)

print(dataframe_csv)

