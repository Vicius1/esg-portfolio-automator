import pandas as pd
from config import *

def calculate_portfolio_metrics(df):
    """
    Recebe o DataFrame, calcula as métricas de performance e formata os resultados.
    """
    print("\nCalculando métricas de performance do portfólio...")

    numeric_cols = [COL_QUANTIDADE, COL_CUSTO_TOTAL, COL_PRECO_ATUAL]
    for col in numeric_cols:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.replace(r"[^\d.]", "", regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df[COL_VALOR_MERCADO] = df[COL_QUANTIDADE] * df[COL_PRECO_ATUAL]

    df[COL_RESULTADO_RS] = df[COL_VALOR_MERCADO] - df[COL_CUSTO_TOTAL]

    df[COL_RESULTADO_PERC] = df.apply(
        lambda row: (row[COL_RESULTADO_RS] / row[COL_CUSTO_TOTAL]) if row[COL_CUSTO_TOTAL] != 0 else 0,
        axis=1
    )
    
    print("Cálculos finalizados.")
    return df

def format_dataframe_for_sheets(df):
    """
    Recebe o DataFrame com dados numéricos e o formata para uma
    exibição amigável na planilha.
    """
    print("Formatando DataFrame para exibição final...")

    df_formatted = df.copy()

    if COL_RESULTADO_PERC in df_formatted.columns:
        df_formatted[COL_RESULTADO_PERC] = df_formatted[COL_RESULTADO_PERC].map("{:.2f}%".format)

    for col in MONEY_COLUMNS:
        if col in df_formatted.columns:
            df_formatted[col] = df_formatted[col].map("R${:,.2f}".format)

    existing_columns = []
    for col in FINAL_COLUMN_ORDER:
        if col in df_formatted.columns:
            existing_columns.append(col)

    return df_formatted[existing_columns]