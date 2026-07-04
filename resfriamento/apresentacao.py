import matplotlib.pyplot as plt

import interpolacao
import mmq

TEMPERATURA_AMBIENTE = 27

def executar(tempos, temperaturas):
    x_interp, y_interp = interpolacao.gerar_curva(
        tempos,
        temperaturas
    )
    # MMQ
    temperaturas_linearizadas = mmq.linearizar(
        temperaturas,
        TEMPERATURA_AMBIENTE
    )

    coeficientes = mmq.mmq_linear(
        tempos,
        temperaturas_linearizadas
    )

    x_mmq, y_mmq = mmq.gerar_curva(
        tempos,
        TEMPERATURA_AMBIENTE,
        coeficientes
    )

    # EQM
    eqm = mmq.erro_quadratico_medio(
        tempos,
        temperaturas,
        TEMPERATURA_AMBIENTE,
        coeficientes
    )

    m, b = coeficientes

    print("=" * 40)
    print("AJUSTE EXPONENCIAL (MMQ)")
    print("=" * 40)
    print(f"Coeficiente angular (m): {m:.6f}")
    print(f"Coeficiente linear  (b): {b:.6f}")
    print(f"EQM: {eqm:.6f}")

    # Gráfico
    plt.figure(figsize=(10, 6))

    plt.scatter(
        tempos,
        temperaturas,
        label="Dados experimentais",
        color="black"
    )

    plt.plot(
        x_interp,
        y_interp,
        label="Interpolação de Lagrange"
    )

    plt.plot(
        x_mmq,
        y_mmq,
        label="MMQ Exponencial"
    )

    plt.xlabel("Tempo (min)")
    plt.ylabel("Temperatura (°C)")
    plt.title("Resfriamento de um corpo")

    plt.grid(True)
    plt.legend()

    plt.show()