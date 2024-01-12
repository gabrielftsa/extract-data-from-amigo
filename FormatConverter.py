import pandas as pd


class FormatConverter:
    @staticmethod
    def excel_para_csv(input_excel, output_csv):
        # A função "read_excel()" lê a planilha Excel e guarda no dataframe
        dataframe = pd.read_excel(input_excel)

        # Exporta o DataFrame modificado para um NOVO arquivo CSV
        dataframe.to_csv(output_csv, index=False)

    @staticmethod
    def csv_para_excel(input_csv, output_excel):
        # A função "read_csv()" lê a planilha Excel e guarda no dataframe
        dataframe_csv = pd.read_csv(input_csv)

        # Exporta o DataFrame do arquivo CSV para uma nova planilha Excel
        dataframe_csv.to_excel(output_excel, index=False, engine='openpyxl')
