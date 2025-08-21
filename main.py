from modules import sheets_handler, data_fetcher, data_processor

def main():
    """
    Função principal que orquestra a execução do script.
    """
    worksheet = sheets_handler.connect_and_get_worksheet()
    if worksheet is None:
        return
    
    portfolio_df = sheets_handler.get_data_as_dataframe(worksheet)
    if portfolio_df.empty:
        print("DataFrame vazio. Verifique a planilha ou a conexão. Encerrando.")
        return

    tickers = portfolio_df["Ticker"].tolist()
    prices = data_fetcher.fetch_market_prices(tickers)
    portfolio_df["Preço Atual"] = prices

    enriched_df = data_fetcher.enrich_with_esg_scores(portfolio_df)

    final_df = data_processor.calculate_portfolio_metrics(enriched_df)

    print("\n--- DataFrame Final Consolidado (Dados Brutos)---")
    print(final_df)
    print("-----------------------------------")

if __name__ == "__main__":
    main()