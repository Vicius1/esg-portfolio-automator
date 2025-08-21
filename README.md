# Dashboard de Portfólio com Google Sheets e Python

![GitHub Actions Workflow Status](https://github.com/Vicius1/esg-portfolio-automator/actions/workflows/run_dashboard.yml/badge.svg)

## 📖 Sobre o Projeto

Este projeto é um pipeline de automação completo que transforma uma simples planilha do Google Sheets em um dashboard dinâmico para acompanhamento de uma carteira de investimentos. O script busca dados de mercado e scores ESG em tempo real, calcula métricas de performance, gera um gráfico de composição da carteira e envia um relatório completo por e-mail.

O projeto foi construído com uma arquitetura modular e segue as melhores práticas de desenvolvimento, como gestão de segredos, logging e automação com CI/CD.

---

## ✨ Funcionalidades Principais

- **Integração com Google Sheets:** Lê a carteira de investimentos diretamente de uma planilha Google e a atualiza com os dados processados.
- **Dados de Mercado em Tempo Real:** Busca cotações atualizadas de ações brasileiras e internacionais usando a API do Yahoo Finance.
- **Enriquecimento de Dados ESG:** Integra pontuações de sustentabilidade (Ambiental, Social e de Governança) a partir de uma fonte de dados local.
- **Cálculo de Performance:** Calcula automaticamente o valor de mercado, o resultado financeiro (R$) e o percentual de retorno (%) para cada ativo.
- **Visualização de Dados:** Gera um gráfico de pizza da composição da carteira por valor de mercado, salvo como um arquivo de imagem.
- **Notificações Automatizadas:** Envia um relatório completo em HTML por e-mail, contendo a tabela de performance e o gráfico como anexo.
- **Logging Detalhado:** Mantém um registro histórico de cada execução em um arquivo de log para fácil depuração e monitoramento.
- **Automação Agendada:** O script é configurado para rodar automaticamente na nuvem em um horário definido através do GitHub Actions.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.11+
- **Bibliotecas Principais:**
  - `pandas`: Para manipulação e análise de dados.
  - `gspread` & `gspread-dataframe`: Para interação com a API do Google Sheets.
  - `yfinance`: Para obtenção de dados do mercado financeiro.
  - `matplotlib`: Para a geração dos gráficos.
  - `python-dotenv`: Para gestão de segredos e variáveis de ambiente.
- **Plataformas:**
  - Google Cloud Platform (para credenciais de API).
  - GitHub & GitHub Actions (para versionamento e automação CI/CD).

---

## 🚀 Como Executar o Projeto

Para configurar e executar este projeto na sua própria máquina, siga os passos abaixo.

### 1. Pré-requisitos

- Python 3.11 ou superior.
- Uma conta Google.
- Uma conta GitHub.

### 2. Configuração do Ambiente

1.  **Clone o Repositório:**
    ```bash
    git clone https://github.com/Vicius1/esg-portfolio-automator.git
    cd esg-portfolio-automator
    ```

2.  **Crie e Ative um Ambiente Virtual:**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Configuração das Credenciais e APIs

1.  **Google Cloud & Sheets API:**
    - Siga um tutorial para criar credenciais de **Conta de Serviço (Service Account)** na Google Cloud Platform.
    - Ative as APIs **Google Drive API** e **Google Sheets API**.
    - Baixe o arquivo de credenciais e renomeie-o para `credentials.json`, colocando-o na pasta raiz do projeto.
    - Crie uma planilha no Google Sheets com as colunas definidas em `config.py`.
    - Compartilhe sua planilha com o e-mail da conta de serviço (`client_email` dentro do `credentials.json`) com permissão de **Editor**.

2.  **Configuração de Segredos (E-mail):**
    - Crie uma **Senha de App** para sua conta Gmail (requer autenticação de 2 fatores ativada).
    - Renomeie o arquivo `.env.example` para `.env`.
    - Preencha o arquivo `.env` com seu e-mail, o e-mail do destinatário e a senha de app gerada:
      ```
      EMAIL_SENDER="seu_email@gmail.com"
      EMAIL_RECEIVER="destinatario@exemplo.com"
      EMAIL_APP_PASSWORD="sua_senha_de_app_de_16_digitos"
      ```

### 4. Uso

1.  **Preencha a Planilha:** Adicione os ativos que você deseja acompanhar na sua planilha do Google Sheets, preenchendo as colunas de input manual (`Ticker`, `Nome da Empresa`, `Quantidade`, `Custo Total`).
2.  **Preencha os Scores ESG:** Adicione os tickers e seus respectivos scores no arquivo `esg_scores.csv`.
3.  **Execute o Script Manualmente:**
    ```bash
    python main.py
    ```
    Ao final da execução, sua planilha será atualizada, um gráfico será gerado e um e-mail de notificação será enviado.

---

## ☁️ Automação com GitHub Actions

Este repositório está configurado para executar o script automaticamente todo dia às 18:00 (horário de Brasília). Para que isso funcione no seu fork/clone, você precisa configurar os **GitHub Secrets**:

1.  Vá em **Settings > Secrets and variables > Actions** no seu repositório.
2.  Crie os seguintes segredos:
    - `GOOGLE_CREDENTIALS`: Cole aqui o **conteúdo completo** do seu arquivo `credentials.json`.
    - `EMAIL_SENDER`: Seu e-mail do Gmail.
    - `EMAIL_RECEIVER`: O e-mail do destinatário.
    - `EMAIL_APP_PASSWORD`: Sua senha de app de 16 dígitos.

O workflow definido em `.github/workflows/run_dashboard.yml` cuidará do resto.
