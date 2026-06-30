# corpo-resfriamento-calc-numerico

Análise de resfriamento de um corpo utilizando Cálculo Numérico Básico.

Este projeto implementa metodos numéricos para modelar o resfriamento de um corpo com base na Lei de Resfriamento de Newton. A lei estabelece que a taxa de perda de calor de um corpo e proporcional a diferenca de temperatura entre o corpo e o ambiente ao seu redor.

A partir de dados experimentais de temperatura ao longo do tempo, o projeto aplica:

- Interpolação de Lagrange para gerar uma curva suave entre os pontos coletados.
- Método dos Mínimos Quadrados (MMQ) para ajustar um modelo exponencial a curva de resfriamento.
- Cálculo do Erro Quadrático Medio (EQM) para avaliar a qualidade do ajuste.
- Visualização gráfica dos resultados com matplotlib.

O modelo ajustado segue a forma T(t) = Ta + (T0 - Ta) * exp(-m * t), onde Ta é a temperatura ambiente, T0 é a temperatura inicial e m é a constante de resfriamento.

## Como rodar

Crie e ative um ambiente virtual:

```console
python -m venv .venv
.venv\Scripts\activate
```

Instale as dependências:

```console
pip install numpy matplotlib jupyter notebook
```

Execute o programa principal:

```console
python resfriamento/calc_numerico.py
```

Ou execute o jupyter notebook para poder visualizar o arquivo .ipynb

```console
jupyter notebook
```

Para sair do ambiente virtual, use o comando `deactivate`.
