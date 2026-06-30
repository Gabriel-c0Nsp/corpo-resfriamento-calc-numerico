import normalizacao
import apresentacao

tempos, temperaturas = normalizacao.carregar_dados("./dados_resfriamento.csv")

apresentacao.executar(tempos, temperaturas)