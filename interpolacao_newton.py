import numpy as np

n = 7  # n representa o numero de termos!
valor_x = 1.5  # valor_x representa o valor de X para qual desejamos encontrar um y no nosso algoritmo

# ------------------------------------
# Definições de cores
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
# -----------------------------------------------------
# Valores iniciais
tabela = {
    # X:Y
    0: 0,
    1: 0.8,
    2: 0.9,
    3: 0.2,
    4: -0.7,
    5: -0.95,
    6: -0.2
}

matrizNewton = np.zeros((n, n))


def setInitialValue():
    i = 0
    for x in tabela:
        matrizNewton[0][i] = tabela.get(x, 0)
        i += 1
# -----------------------------------------------------
# Calculos

# Funcao para calcular os (x-x0)*(x-xn)
def auxCalcPol(i, x):
    resultado = 1
    count = 0
    for xn in tabela:
        if count == i:  # Teste particular da linguagem python para garantir a intregridade do codigo
            break
        resultado *= (x - xn)
        count += 1

    return resultado

# Funcao que representa a formula de newton para encontrar o polinomeio interpolador
def calculoPolinomial(i, x):
    if (i == n):
        return 0
    else:
        resultado = (matrizNewton[i][0] * auxCalcPol(i, x)
                     ) + calculoPolinomial((i+1), x)
        return resultado


def diferencaDividida(linha, coluna):
    # linha representa as fases para a interpolacao de newton, por exemplo,
    # para um grau 6 eh nescessario 6 etapas, para tanto somamos a coluna com a linha para obter
    # a diferença correta para os valores de xa e xb
    xa = list(tabela.keys())[(coluna + linha)]
    xb = list(tabela.keys())[(coluna)]

    linhaAnt = (linha - 1)
    resultado = (matrizNewton[linhaAnt][coluna + 1] -
                 matrizNewton[linhaAnt][coluna]) / (xa - xb)
    matrizNewton[linha][coluna] = resultado


# Procedimento para mostrar os valores da tabela de coeficientes
def showTable():
    for i in range(0, n):
        for j in range(n - i):
            if j == 0:
                print("[" + GREEN + str(round(matrizNewton[i][j], 4)) +
                      RESET + "], ", "\t", end=" ")
            else:
                print("[" + str(round(matrizNewton[i][j], 4)) + "], ",
                      "\t", end=" ")
        print("")


# main
setInitialValue()

for i in range(1, n):
    for j in range(n - i):
        diferencaDividida((i), j)
showTable()

print("O valor estimado para Y(", GREEN, valor_x, RESET, ") pelo polinomio interpolador de newton é: ", GREEN,
      round(calculoPolinomial(0, valor_x), 4), RESET)
