import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point

def curva_de_capacidade(v_nom_linha, fp, p, xd):
    """
    Gera a curva de capacidade (plano P x Q) de uma máquina síncrona.

    Parâmetros:
    v_nom_linha (float): Tensão nominal de linha (V).
    fp (float): Fator de potência da carga.
    p (float): Potência ativa (W).
    xd (float): Reatância síncrona (pu).

    Retorna:
    None: Exibe o gráfico da curva de capacidade.
    """
    
    v_nom_fase = v_nom_linha / np.sqrt(3)
    s = p / fp

    Z_base = v_nom_linha ** 2 / s
    xs = xd * Z_base
    
    i_a = (s / (np.sqrt(3) * v_nom_linha)) * np.exp(1j * (-np.arccos(fp)))
    i_a_modulo = np.abs(i_a)

    Eaf = v_nom_fase + 1j * xs * i_a_modulo
    Eaf_modulo = np.abs(Eaf)

    S_g = (3 * v_nom_fase * i_a_modulo) / 1000 
    raio_est = S_g
    centro_est = (0, 0)

    Q_g = -(3 * v_nom_fase ** 2 / xs) / 1000
    raio_rot = (3 * v_nom_fase * Eaf_modulo / xs) / 1000

    centro_rot = (0, Q_g)

    theta = np.linspace(0, 2 * np.pi, 600)
    x_est = centro_est[0] + raio_est * np.cos(theta)
    y_est = centro_est[1] + raio_est * np.sin(theta)

    x_rot = centro_rot[0] + raio_rot * np.cos(theta)
    y_rot = centro_rot[1] + raio_rot * np.sin(theta)

    circle_estator = Point(centro_est).buffer(raio_est)
    circle_rotor = Point(centro_rot).buffer(raio_rot)

    intersec = circle_estator.intersection(circle_rotor)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_aspect('equal')
    ax.grid(True)

    ax.fill(x_est, y_est, color='blue', alpha=0.8, label='Limite do Estator')
    ax.fill(x_rot, y_rot, color='red', alpha=0.8, label='Limite do Rotor')

    if not intersec.is_empty:
        x_inter, y_inter = intersec.exterior.xy
        ax.fill(x_inter, y_inter, color='purple', alpha=0.8, label='Capacidade da Máquina')

    margem = 1.2
    ax.set_xlim(-S_g * margem, S_g * margem)
    ax.set_ylim(-S_g * margem, S_g * margem)

    plt.title('Curva de Capacidade — Plano P x Q', fontsize=12)
    plt.xlabel('P (kW)', fontsize=11)
    plt.ylabel('Q (kVAr)', fontsize=11)
    plt.legend(loc='best')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()

curva_de_capacidade(380, 0.85, 451e3, 4.624)
