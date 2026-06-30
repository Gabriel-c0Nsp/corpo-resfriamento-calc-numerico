import csv

def carregar_dados(caminho):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        dados = [(int(linha['tempo_min']), float(linha['temperatura_c'])) for linha in leitor]

        tempos, temperaturas = zip(*dados)

        return list(tempos), list(temperaturas)