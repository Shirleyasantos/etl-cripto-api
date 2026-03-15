import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def extrair_dados():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    resposta = requests.get(url)
    return resposta.json()

def transformar_dados(dados_brutos):
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
    engine = create_engine('sqlite:///crypto_data.db')
    df.to_sql('precos_cripto', con=engine, if_exists='append', index=False)

if __name__ == "__main__":
    print("Iniciando a pipeline...")
    dados = extrair_dados()
    df_limpo = transformar_dados(dados)
    carregar_dados(df_limpo)
    print("Dados processados e salvos com sucesso!")
