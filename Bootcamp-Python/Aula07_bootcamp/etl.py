import csv

path_arquivo = r"C:\Users\Estudos\Desktop\DATA ENGINEER\01 - Python\Python-Estudos\Bootcamp-Python\Aula07_bootcamp\vendas.csv"


def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários
    """
    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    """
    Função que filtra produtos onde entrega = True
    """
    lista_com_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_com_produtos_filtrados.append(produto)
    return lista_com_produtos_filtrados


def soma_valores_dos_produtos(lista: list[dict]) -> int:
    """
    Função que soma os valores de todos os produtos que estão na lista
    """
    valor_total_dos_produtos = 0
    for produto in lista:
        valor_total_dos_produtos += int(produto.get("price"))
    return valor_total_dos_produtos


