import logging
from modules import sheets_handler, data_fetcher, data_processor
from config import COL_TICKER, COL_PRECO_ATUAL

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("portfolio_dashboard.log", mode='w'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    """
    Função principal que orquestra a execução do script.
    """
    logger.info("--- Iniciando execução do dashboard portfólio ---")

    worksheet = sheets_handler.connect_and_get_worksheet()
    if worksheet is None:
        logger.critical("Conexão com a planilha falhou. Encerrando programa.")
        return
    
    portfolio_df = sheets_handler.get_data_as_dataframe(worksheet)
    if portfolio_df.empty:
        logger.warning("DataFrame vazio. Verifique a planilha ou a conexão. Encerrando.")
        return

    tickers = portfolio_df[COL_TICKER].tolist()
    prices = data_fetcher.fetch_market_prices(tickers)
    portfolio_df[COL_PRECO_ATUAL] = prices

    enriched_df = data_fetcher.enrich_with_esg_scores(portfolio_df)

    processed_df = data_processor.calculate_portfolio_metrics(enriched_df)

    formatted_df = data_processor.format_dataframe_for_sheets(processed_df)

    sheets_handler.update_worksheet(worksheet, formatted_df)

    logger.info("--- Execução finalizada com sucesso ---")

if __name__ == "__main__":
    main()