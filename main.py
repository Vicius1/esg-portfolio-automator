import gspread
import pandas as pd

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

gc = gspread.service_account(filename='credentials.json', scopes=SCOPES)

try:
    spreadsheet = gc.open("Dashboard_Portfolio")
    print("Conectado à planilha com sucesso!")
    worksheet = spreadsheet.sheet1
    print(f"Acessando a aba: '{worksheet.title}'")

    data = worksheet.get_all_records()

    df = pd.DataFrame(data)
    print("Dados carregados da planilha para o DataFrame:")
    print(df.head())

except gspread.exceptions.SpreadsheetNotFound:
    print("ERRO: Planilha não encontrada. Verifique os seguintes pontos:")
    print("1. O nome da planilha no código está EXATAMENTE igual ao nome no Google Sheets?")
    print("2. Você compartilhou a planilha com o 'client_email' do seu arquivo credentials.json com permissão de 'Editor'?")