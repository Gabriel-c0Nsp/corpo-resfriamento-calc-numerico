import interpolacao
import normalizacao

tempos, temperaturas = normalizacao.carregar_dados("./dados_resfriamento.csv")

valor = interpolacao.lagrange(tempos, temperaturas, 5)
print(valor)