from etl import pipeline_calculo_de_vendas


pasta_argumento = r'C:\Users\Estudos\Desktop\DATA ENGINEER\01 - Python\Python-Estudos\Bootcamp-Python\Aula08_bootcamp\data' # Caminho onde está os arquivos JSON
formato: list = ['csv', 'parquet']

pipeline_calculo_de_vendas(pasta=pasta_argumento, formato_de_saida=formato)

