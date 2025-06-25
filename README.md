# Análise de Gerador Síncrono em Regime Estacionário

Este repositório contém a implementação em Python das simulações exigidas na Avaliação 4 da disciplina **Conversão Eletromecânica de Energia II**, do curso de Engenharia Elétrica da UFERSA.

---

## 🧠 Objetivo

Simular o comportamento de um gerador síncrono alimentando uma carga específica, utilizando modelos matemáticos para analisar:
- Curva V
- Curva de Capacidade (plano P-Q)
- Relação entre ângulo da tensão induzida (δ) e potência ativa (P_g)

---

## ⚙️ Dados Utilizados

- **Gerador:** WEG AG10250SI10CI B3T IP23
- **Tensão nominal:** 380 V (trifásica)
- **Reatância síncrona eixo direto (Xd):** 4.146 pu
- **Reatância síncrona eixo em quadratura (Xq):** 1.146 pu
- **Potência ativa da carga:** 86 kW
- **Fator de potência:** 0.85 (indutivo)

---

## 🧪 Simulações

### ✔️ Questão 2 — Curva V

- Mostra a relação entre a corrente de campo (If) e a corrente de armadura (Ia) para 25%, 50%, 75% e 100% da carga.

### ✔️ Questão 3 — Curva de Capacidade (P x Q)

- Exibe os limites operacionais do gerador no plano da potência ativa (P) e reativa (Q), destacando as regiões de atuação da armadura e do rotor.

### ✔️ Questão 4 — Ângulo δ x Potência Ativa

- Mostra como o ângulo da tensão induzida (δ) varia com o aumento da potência ativa, para diferentes fatores de potência.

---

## 🧰 Bibliotecas Utilizadas

- `numpy`
- `matplotlib`
- `shapely` (apenas para interseção de áreas na curva de capacidade)
