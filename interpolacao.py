from math import prod as produtorio
from numpy import linspace
somatorio = sum

def lagrange(x, y, ponto):
    return somatorio(
        y[i] * produtorio(
            (ponto - x[j]) / (x[i] - x[j])

            # len(x) = n
            for j in range(len(x))
            if i != j
        )
        for i in range(len(x))
    )

def gerar_curva(x, y, quantidade=500):

    eixo_x = linspace(min(x), max(x), quantidade)

    eixo_y = [
        lagrange(x, y, ponto)
        for ponto in eixo_x
    ]

    return eixo_x, eixo_y