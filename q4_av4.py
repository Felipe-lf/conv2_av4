import numpy as np
import matplotlib.pyplot as plt

def curva_delta_vs_p(v_linha, p_ativa, fp, xq_pu):
    """
    Gera a curva do ângulo da tensão induzida (δ) em função da potência ativa (P)
    para diferentes fatores de potência no modo indutivo.

    Parâmetros:
    v_linha (float): Tensão nominal de linha (V).
    p_ativa (float): Potência ativa (W).
    fp (float): Fator de potência mínimo (ex.: 0.85).
    xq_pu (float): Reatância síncrona de eixo em quadratura (pu).

    Retorna:
    None: Exibe o gráfico da curva δ x P_g.
    """

    s = p_ativa / fp

    z_base = (v_linha ** 2) / s
    xq = xq_pu * z_base

    fp_list = [1.0, 0.95, 0.9, fp]

    plt.figure(figsize=(8, 6))
    plt.grid(True)

    for fp_atual in fp_list:
        ang_pot = np.arccos(fp_atual)
        p_g = s * fp_atual             

        valores_p = np.linspace(0, p_g, 100)
        ang_delta = []                        

        for p in valores_p:
            i_a = p / (np.sqrt(3) * v_linha * fp_atual)

            num = i_a * xq * np.cos(ang_pot)
            den = v_linha - i_a * xq * np.sin(ang_pot)

            delta = np.degrees(np.arctan2(num, den))
            ang_delta.append(delta)

        plt.plot(valores_p / 1000, ang_delta, linewidth=1.5)

    plt.title('δ (Graus) x P_g (kW)', fontsize=12)
    plt.xlabel('Potência Ativa (kW)', fontsize=11)
    plt.ylabel('Ângulo da Tensão Induzida δ (graus)', fontsize=11)

    plt.legend([f'FP={fp}' for fp in fp_list], loc='best')

    margem_x = (s * max(fp_list)) / 1000 * 1.2
    margem_y = max(ang_delta) * 1.2 if ang_delta else 100

    plt.xlim(0, margem_x)
    plt.ylim(0, margem_y)

    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()

curva_delta_vs_p(380,86000,0.85,1.146)
