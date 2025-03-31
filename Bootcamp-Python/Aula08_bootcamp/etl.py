import pandas as pd 
import os 
import glob


def extrair_dados(pasta: str) -> pd.DataFrame:
    """
    Extrai e concatena dados de arquivos JSON em um único DataFrame.
    """
    arquivos_json = glob.glob(os.path.join(pasta, '*.json')) # Lista com os caminhos completos de todos os arquivos JSON dentro da pasta desejada
    df_list = []                                             # Lista vazia para salvar o DF
    for arquivo in arquivos_json:                            # For para armaenar todos os arquivos em apenas um DF
        df_list.append(pd.read_json(arquivo))                # Armazenando os valores do DF na lista total
    df_total = pd.concat(df_list, ignore_index=True)         # Concatenando todos os valores armazenados
    return df_total                                          # Retornando o DF


def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona uma nova coluna 'Total' ao DataFrame, calculando o total de vendas de cada produto:
    Total = Quantidade * Venda
    """
    df["Total"] = df["Quantidade"] * df["Venda"]            # Criando uma nova coluna
    return df                                               # Retornando o DF


def carregar_dados(df: pd.DataFrame, formato_saida: list):
    """
    Salva um DataFrame em um ou mais formatos especificados.

    Parâmetros:
        df (pd.DataFrame): DataFrame a ser salvo.
        formatos_saida (list): Lista de formatos desejados (ex.: ['csv', 'parquet']).

    Retorno:
        None
    """
    if 'csv' in formato_saida:                              # Verificando se na lista tem o formato CSV   
        df.to_csv("dados.csv")                              # Carregando os dados em um arquivo CSV
    if 'parquet' in formato_saida:                          # Verificando se na lista tem o formato PARQUET
        df.to_parquet("dados.parquet")                      # Carregando so dados em um arquivo PARQUET


def pipeline_calculo_de_vendas(pasta: str, formato_de_saida: list):
    """
    Executa um pipeline ETL para cálculo de vendas:
    
    1. Extrai os dados de arquivos JSON dentro da pasta especificada.
    2. Calcula o KPI de total de vendas (Quantidade * Venda).
    3. Salva os dados no(s) formato(s) especificado(s).

    Parâmetros:
        pasta (str): Caminho da pasta contendo arquivos JSON.
        formatos_de_saida (list): Lista de formatos para salvar os dados (ex.: ['csv', 'parquet']).
    
    Retorno:
        None
    """
    data_frame = extrair_dados(pasta) 
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)


