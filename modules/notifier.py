import os
import logging
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import re
from config import EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_APP_PASSWORD, COL_TICKER

logger = logging.getLogger(__name__)

def _clean_dataframe_for_email(df):
    """Limpa e prepara o DataFrame para ser convertido em HTML."""
    df_cleaned = df.copy()
    df_cleaned[COL_TICKER] = df_cleaned[COL_TICKER].astype(str).str.replace('.', '.\u200c', regex=False)
    return df_cleaned

def _create_html_body(df):
    """Cria o conteúdo HTML do corpo do e-mail a partir de um DataFrame."""
    html_table = df.to_html(index=False, justify='center', render_links=False)
    html_body = f"""
    <html>
        <body>
            <h2>Olá!</h2>
            <p>Seu script de automação foi executado com sucesso. Aqui está o resumo do seu portfólio:</p>
            {html_table}
            <p>A composição da sua carteira está anexada a este e-mail.</p>
            <p>Atenciosamente,<br>Seu Robô de Portfólio Python</p>
        </body>
    </html>
    """
    return html_body

def _attach_image(message, image_path):
    """Anexa uma imagem ao objeto de mensagem de e-mail."""
    try:
        attachment_name = os.path.basename(image_path)
        
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()
        
        image = MIMEImage(image_data, name=attachment_name)
        message.attach(image)
        logger.info(f"Anexou o gráfico '{image_path}' ao e-mail com sucesso.")
    except FileNotFoundError:
        logger.warning(f"Arquivo de imagem '{image_path}' não encontrado. O e-mail será enviado sem o anexo.")
    except Exception as e:
        logger.error(f"Não foi possível anexar a imagem do gráfico: {e}", exc_info=True)
    return message

def _send_message_via_smtp(message):
    """Conecta-se ao servidor SMTP do Gmail e envia a mensagem."""
    context = ssl.create_default_context()
    try:
        logger.info(f"Conectando ao servidor SMTP do Gmail para enviar e-mail para {EMAIL_RECEIVER}...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(EMAIL_SENDER, EMAIL_APP_PASSWORD)
            server.send_message(message)
        logger.info("E-mail de notificação enviado com sucesso!")
    except Exception as e:
        logger.error(f"Falha ao enviar e-mail de notificação: {e}", exc_info=True)

def send_email_notification(df, image_path):
    """
    Orquestra a criação e o envio de um e-mail de notificação com o resumo do portfólio.
    """
    logger.info("Iniciando o processo de notificação por e-mail...")

    cleaned_df = _clean_dataframe_for_email(df)
    html_body = _create_html_body(cleaned_df)
    subject = "Relatório Diário do seu Portfólio de Impacto"

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = EMAIL_SENDER
    message['To'] = EMAIL_RECEIVER
    message.attach(MIMEText(html_body, "html"))

    message = _attach_image(message, image_path)

    _send_message_via_smtp(message)