import yfinance as yf
import pandas as pd
from config import ESG_SCORES_CSV, COL_TICKER, COL_SCORE_ESG
import logging

logger = logging.getLogger(__name__)

def fetch_market_prices(tickers_list):
    """
    Busca os preços atuais de mercado para uma lista de tickers,
    usando uma única chamada de API
    """
    logger.info("Buscando preços atuais das ações...")
    try:
        data = yf.download(tickers=tickers_list, period="1d", progress=False, auto_adjust=True)
        prices = data["Close"].iloc[-1]
        ordered_prices = prices.reindex(tickers_list).fillna(0)

        logger.info("Preços obtidos com sucesso!")
        return ordered_prices.tolist()
    except Exception as e:
        logger.error(f"Erro ao buscar preços: {e}", exc_info=True)
        return [0] * len(tickers_list)

def enrich_with_esg_scores(main_df):
    """
    Enriquece o DataFrame principal com scores ESG de um arquivo CSV.
    """
    logger.info("Enriquecendo dados com Scores ESG...")

    if COL_SCORE_ESG in main_df.columns:
        main_df = main_df.drop(columns=[COL_SCORE_ESG])

    try:
        esg_df = pd.read_csv(ESG_SCORES_CSV)
        enriched_df = pd.merge(main_df, esg_df, on=COL_TICKER, how="left")
        logger.info("DataFrame enriquecido com dados ESG.")
        return enriched_df
    except FileNotFoundError:
        logger.warning(f"AVISO: Arquivo \"{ESG_SCORES_CSV}\" não encontrado. A coluna ESG será preenchida com 'N/A'.")
        main_df[COL_SCORE_ESG] = "N/A"
        return main_df