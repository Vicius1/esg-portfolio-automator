import yfinance as yf
import pandas as pd
from config import ESG_SCORES_CSV

def fetch_market_prices(tickers_list):
    """
    Busca os preços atuais de mercado para uma lista de tickers.
    """
    print("\nBuscando preços atuais das ações...")
    prices = []
    for ticker_symbol in tickers_list:
        try:
            ticker = yf.Ticker(ticker_symbol)
            price = ticker.info.get("currentPrice")
            if price is None:
                raise ValueError("Preço não encontrado")
            prices.append(price)
            print(f"  - {ticker_symbol}: R$ {price}")
        except Exception:
            print(f"  - ERRO: Não foi possível obter o preço para {ticker_symbol}")
            prices.append(0)
    return prices

def enrich_with_esg_scores(main_df):
    """
    Enriquece o DataFrame principal com scores ESG de um arquivo CSV.
    """
    print("\nEnriquecendo dados com Scores ESG...")
    try:
        esg_df = pd.read_csv(ESG_SCORES_CSV)
        enriched_df = pd.merge(main_df, esg_df, on="Ticker", how="left")
        print("DataFrame enriquecido com dados ESG.")
        return enriched_df
    except FileNotFoundError:
        print(f"AVISO: Arquivo \"{ESG_SCORES_CSV}\" não encontrado.")
        main_df["Score ESG"] = "N/A"
        return main_df