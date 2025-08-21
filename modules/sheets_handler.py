import gspread
import pandas as pd
from gspread_dataframe import set_with_dataframe
from config import SCOPES, CREDENTIALS_FILE, SHEET_NAME

def connect_and_get_worksheet():
    """
    Conecta-se à API do Google Sheets usando as credenciais e retorna
    um objeto da aba da planilha.
    """
    try:
        gc = gspread.service_account(filename=CREDENTIALS_FILE, scopes=SCOPES)
        spreadsheet = gc.open(SHEET_NAME)
        worksheet = spreadsheet.sheet1
        print(f"Conectado com sucesso à planilha \"{SHEET_NAME}\", aba \"{worksheet.title}\".")
        return worksheet
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"ERRO: Planilha \"{SHEET_NAME}\" não encontrada.")
        print("Verifique o nome e as permissões de compartilhamento.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado na conexão com o Sheets: {e}")
        return None

def get_data_as_dataframe(worksheet):
    """
    Recebe um objeto de aba e retorna os dados como um DataFrame do Pandas.
    """
    if worksheet is None:
        return pd.DataFrame()
        
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
    print("Dados da planilha carregados para o DataFrame.")
    return df

def update_worksheet(worksheet, df):
    """
    Recebe o DataFrame formatado e o escreve na planilha.
    """
    print("\nIniciando a atualização da planilha...")
    if worksheet is None:
        print("ERRO: Worksheet não encontrado.")
        return

    try:
        set_with_dataframe(worksheet, df, resize=False)
        
        print("Planilha atualizada com sucesso! Verifique o resultado no seu Google Sheets")
    except Exception as e:
        print(f"ERRO: Não foi possível atualizar a planilha: {e}")