from math import prod as produtorio
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