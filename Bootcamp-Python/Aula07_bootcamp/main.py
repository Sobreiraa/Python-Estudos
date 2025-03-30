from etl import ler_csv, filtrar_produtos_nao_entregues, soma_valores_dos_produtos

path_arquivo = r"C:\Users\Estudos\Desktop\DATA ENGINEER\01 - Python\Python-Estudos\Bootcamp-Python\Aula07_bootcamp\vendas.csv"

lista_de_produtos = ler_csv(path_arquivo)
lista_de_produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)
total_vendido = soma_valores_dos_produtos(lista_de_produtos)

print(lista_de_produtos_entregues)
print(total_vendido)