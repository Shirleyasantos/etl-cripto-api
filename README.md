# etl-cripto-api
Pipeline de extração de dados da API CoinGecko e armazenamento em SQLite
# 🪙 Pipeline de Dados: Monitoramento de Criptomoedas

Este é um projeto de **Engenharia de Dados** que demonstra um fluxo completo de ETL (Extração, Transformação e Carga). O objetivo é coletar preços de mercado de Bitcoin e Ethereum para futuras análises históricas.

## 🚀 Arquitetura da Pipeline
1. **Extração:** Coleta de dados em tempo real via API REST da CoinGecko utilizando a biblioteca `requests`.
2. **Transformação:** Processamento dos dados brutos (JSON) para formato tabular com `Pandas`, incluindo a criação de campos de data/hora (timestamp).
3. **Carga:** Armazenamento dos dados limpos em um banco de dados relacional **SQLite** via `SQLAlchemy`.



## 🛠️ Tecnologias Utilizadas
* **Python 3.10+**
* **Pandas**: Manipulação e limpeza de dados.
* **SQLAlchemy**: Interface com o banco de dados.
* **Requests**: Comunicação com APIs externas.
* **SQLite**: Armazenamento leve e eficiente.

## 📈 Como rodar o projeto
1. Clone o repositório.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute o script: `python pipeline.py`.
4. Verifique o arquivo `crypto_data.db` gerado.

---
*Projeto desenvolvido para fins de estudo em Engenharia de Dados.*
