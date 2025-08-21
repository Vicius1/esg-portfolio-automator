import logging
import matplotlib.pyplot as plt
from config import COL_TICKER, COL_VALOR_MERCADO

logger = logging.getLogger(__name__)

def create_portfolio_pie_chart(df, filename="portfolio_composition.png"):
    """
    Cria e salva um gráfico de pizza da composição do portfólio por valor de mercado.

    Args:
        df (pd.DataFrame): DataFrame contendo os dados do portfólio.
                            Deve conter as colunas COL_TICKER e COL_VALOR_MERCADO.
        filename (str): Nome do arquivo para salvar o gráfico.
    """
    logger.info("Criando gráfico de pizza da composição do portfólio...")

    try:
        market_values = df[COL_VALOR_MERCADO]
        tickers = df[COL_TICKER]

        plt.figure(figsize=(10, 8))
        plt.pie(market_values, labels=tickers, autopct='%1.1f%%', startangle=140)
        plt.title("Composição do Portfólio por Valor de Mercado", fontsize=16)
        plt.axis('equal')

        plt.savefig(filename)
        logger.info(f"Gráfico salvo com sucesso como {filename}")
        plt.close()
    except Exception as e:
        logger.error(f"Erro ao criar gráfico de pizza: {e}", exc_info=True)