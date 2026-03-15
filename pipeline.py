import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def extrair_dados():
    """Extrai dados da API da CoinGecko"""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    resposta = requests.get(url)
    return resposta.json()

def transformar_dados(dados_brutos):
    """Transforma o JSON em um DataFrame organizado"""
    preco_btc = dados_brutos['bitcoin']['usd']
    preco_eth = dados_brutos['ethereum']['usd']
    
    lista_dados = [
        {'moeda': 'bitcoin', 'preco_usd': preco_btc},
        {'moeda': 'ethereum', 'preco_usd': preco_eth}
    ]
    
    df = pd.DataFrame(lista_dados)
    df['data_coleta'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return df

def carregar_dados(df):
    """Salva os dados em um banco de dados SQLite"""
    engine = create_engine('sqlite:///crypto_data.db')
    df.to_sql('precos_cripto', con=engine, if_exists='append', index=False)

if __name__ == "__main__":
    # Fluxo principal da Pipeline
    print("Iniciando a extração...")
    dados = extrair_dados()
    
    print("Iniciando a transformação...")
    df_limpo = transformar_dados(dados)
    
    print("Carregando dados no banco...")
    carregar_dados(df_limpo)
    
    print("Pipeline finalizada com sucesso!")
