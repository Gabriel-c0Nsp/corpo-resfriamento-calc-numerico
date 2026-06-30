from math import exp, log
import numpy as np
somatorio = sum


def linearizar(temperaturas, temperatura_ambiente):
    """
    Calcula ln(T - Ta) para cada temperatura.
    """
    return [
        log(temperatura - temperatura_ambiente)
        for temperatura in temperaturas
    ]


def mmq_linear(x, y):
    """
    Ajuste linear por mínimos quadrados.
    """

    n = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    
    soma_xy = sum(
        xi * yi
        for xi, yi in zip(x, y)
    )

    soma_x2 = sum(
        xi ** 2
        for xi in x
    )

    m = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)

    b = (soma_y - m * soma_x) / n

    return (m, b)


def modelo_exponencial(tempo, temperatura_ambiente, coeficientes):
    """
    Reconstrói o modelo exponencial.

    ln(T - Ta) = m*t + b
    """
    m, b = coeficientes

    return temperatura_ambiente + exp(m * tempo + b)
    
def erro_quadratico_medio(
    tempos,
    temperaturas,
    temperatura_ambiente,
    coeficientes
):
    return somatorio(
        (
            temperatura_real
            - modelo_exponencial(
                tempo,
                temperatura_ambiente,
                coeficientes
            )
        ) ** 2
        
        for tempo, temperatura_real in zip(
            tempos,
            temperaturas
        )
    ) / len(tempos)


def gerar_curva(tempos, temperatura_ambiente, coeficientes, quantidade=500):
    eixo_x = np.linspace(min(tempos), max(tempos), quantidade)

    eixo_y = [
        modelo_exponencial(
            ponto,
            temperatura_ambiente,
            coeficientes
        )
        for ponto in eixo_x
    ]

    return eixo_x, eixo_y