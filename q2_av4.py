import numpy as np
import matplotlib.pyplot as plt

def curvas_tipo_V(xd, xq, va, fp, cte_cca):

    """
    Gera a curva V de uma máquina síncrona de polos salientes.

    A curva V relaciona a corrente de campo (If) com a corrente de armadura (Ia)
    para diferentes níveis de potência ativa (25%, 50%, 75% e 100%) operando com
    um fator de potência específico.

    Parâmetros:
    xd (float): Reatância síncrona no eixo direto (pu).
    xq (float): Reatância síncrona no eixo em quadratura (pu).
    va (float): Tensão terminal (pu), normalmente 1 pu.
    fp (float): Fator de potência da operação (ex.: 0.85).
    cte_cca (float): Constante que relaciona a tensão induzida com a corrente de campo.

    Retorna:
    None: Exibe um gráfico da curva V com a relação entre If (corrente de campo) 
    e Ia (corrente de armadura) para diferentes cargas.
    """

    theta = np.arccos(fp) * np.arange(1, -1.1, -0.1)
    porcentagem_de_P = np.array([0.25, 0.5, 0.75, 1.0])

    plt.figure(figsize=(8, 6))
    plt.grid(True)

    for p in porcentagem_de_P:
        i_a = p / (va * np.cos(theta))

        E_af = va + 1j * (xq * i_a * np.exp(1j * theta))
        fase_E_af = np.angle(E_af)

        i_d = i_a * np.sin(theta + fase_E_af) * np.exp(1j * (fase_E_af - np.pi / 2))
        i_q = i_a * np.cos(theta + fase_E_af) * np.exp(1j * fase_E_af)

        E_af = va + 1j * (xd * i_d + xq * i_q)

        i_f = cte_cca * np.abs(E_af)

        plt.plot(i_f, i_a, linewidth=1.5)

    plt.title('Curva V — I_a (pu) x I_f (A)', fontsize=12)
    plt.xlabel('Corrente de Campo (A)', fontsize=11)
    plt.ylabel('Corrente de Armadura (pu)', fontsize=11)
    plt.legend(['P 25%', 'P 50%', 'P 75%', 'P 100%'], loc='best')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()

    return plt.show()


curvas_tipo_V(4.146, 1.146, 1, 0.85, 0.8)
