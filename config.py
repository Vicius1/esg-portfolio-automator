SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
CREDENTIALS_FILE = "credentials.json"
SHEET_NAME = "Dashboard_Portfolio"

ESG_SCORES_CSV = "esg_scores.csv"

COL_TICKER = "Ticker"
COL_NOME_EMPRESA = "Nome da Empresa"
COL_QUANTIDADE = "Quantidade"
COL_CUSTO_TOTAL = "Custo Total"

COL_PRECO_ATUAL = "Preço Atual"
COL_VALOR_MERCADO = "Valor de Mercado"
COL_RESULTADO_RS = "Resultado (R$)"
COL_RESULTADO_PERC = "Resultado (%)"
COL_SCORE_ESG = "Score ESG"

FINAL_COLUMN_ORDER = [
    COL_TICKER, COL_NOME_EMPRESA, COL_QUANTIDADE, COL_CUSTO_TOTAL,
    COL_PRECO_ATUAL, COL_VALOR_MERCADO, COL_RESULTADO_RS,
    COL_RESULTADO_PERC, COL_SCORE_ESG
]

MONEY_COLUMNS = [
    COL_CUSTO_TOTAL, COL_PRECO_ATUAL, COL_VALOR_MERCADO, COL_RESULTADO_RS
]