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