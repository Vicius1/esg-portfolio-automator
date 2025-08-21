import pandas as pd

def calculate_portfolio_metrics(df):
    """
    Recebe o DataFrame, calcula as métricas de performance e formata os resultados.
    """
    print("\nCalculando métricas de performance do portfólio...")

    numeric_cols = ["Quantidade", "Custo Total", "Preço Atual"]
    for col in numeric_cols:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.replace(r"[^\d.]", "", regex=True)
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["Valor de Mercado"] = df["Quantidade"] * df["Preço Atual"]

    df["Resultado (R$)"] = df["Valor de Mercado"] - df["Custo Total"]

    df["Resultado (%)"] = df.apply(
        lambda row: (row["Resultado (R$)"] / row["Custo Total"]) if row["Custo Total"] != 0 else 0,
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

    if "Resultado (%)" in df_formatted.columns:
        df_formatted["Resultado (%)"] = df_formatted["Resultado (%)"].map("{:.2f}%".format)

    money_columns = ["Custo Total", "Preço Atual", "Valor de Mercado", "Resultado (R$)"]
    for col in money_columns:
        if col in df_formatted.columns:
            df_formatted[col] = df_formatted[col].map("R${:,.2f}".format)

    final_columns_order = [
        "Ticker", "Nome da Empresa", "Quantidade", "Custo Total", "Preço Atual",
        "Valor de Mercado", "Resultado (R$)", "Resultado (%)", "Score ESG"
    ]

    existing_columns = []
    for col in final_columns_order:
        if col in df_formatted.columns:
            existing_columns.append(col)

    return df_formatted[existing_columns]