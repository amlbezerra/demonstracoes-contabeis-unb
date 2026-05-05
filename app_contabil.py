import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import base64
from pathlib import Path

st.set_page_config(page_title="DCF / UnB", layout="wide")


# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(30, 99, 160, 0.45), transparent 35%),
        linear-gradient(135deg, #06182c 0%, #092d44 48%, #0b5d49 100%);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #06182c 0%, #07304a 55%, #0a5a45 100%);
    border-right: 1px solid rgba(255,255,255,0.22);
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.block-container {
    padding-top: 1.8rem;
    padding-left: 2.2rem;
    padding-right: 2.2rem;
    padding-bottom: 2rem;
}

h1, h2, h3, h4, p, label, span {
    color: white !important;
}

.bloco {
    background: rgba(8, 27, 47, 0.58);
    padding: 24px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.14);
    margin-top: 12px;
    margin-bottom: 18px;
}

.dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 22px;
}

.dashboard-title h1 {
    font-size: 40px;
    font-weight: 900;
    margin: 0;
    letter-spacing: -1px;
}

.dashboard-title p {
    color: #6ee35d !important;
    font-size: 17px;
    font-weight: 700;
    margin-top: 6px;
}

.exercise-box {
    border: 1px solid rgba(255,255,255,0.28);
    border-radius: 12px;
    padding: 14px 22px;
    background: rgba(7, 24, 44, 0.72);
    font-weight: 700;
    min-width: 160px;
    text-align: center;
}

.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 18px;
    margin-bottom: 18px;
}

.kpi-card {
    background: rgba(7, 28, 48, 0.78);
    border: 1px solid rgba(137, 190, 230, 0.28);
    border-radius: 16px;
    padding: 24px;
    display: flex;
    gap: 20px;
    align-items: center;
    min-height: 112px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.22);
}

.kpi-icon {
    width: 72px;
    height: 72px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
}

.kpi-icon.green { background: linear-gradient(135deg, #0bb85d, #047a45); }
.kpi-icon.blue { background: linear-gradient(135deg, #1d7ff0, #044d9b); }
.kpi-icon.red { background: linear-gradient(135deg, #c94040, #8b2525); }

.kpi-symbol {
    font-size: 34px;
    font-weight: 900;
}

.kpi-label {
    font-size: 14px;
    font-weight: 800;
    color: rgba(255,255,255,0.82) !important;
    text-transform: uppercase;
}

.kpi-value {
    font-size: 30px;
    font-weight: 900;
    margin-top: 4px;
}

.kpi-value.green { color: #55d85a !important; }
.kpi-value.blue { color: #3f92ff !important; }
.kpi-value.red { color: #ff5c5c !important; }

.kpi-change {
    margin-top: 6px;
    font-size: 14px;
    font-weight: 800;
}

.kpi-change.red { color: #ff5151 !important; }
.kpi-change.green { color: #55d85a !important; }

.panel-card {
    background: rgba(7, 28, 48, 0.78);
    border: 1px solid rgba(137, 190, 230, 0.28);
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.22);
}

.panel-title {
    font-size: 18px;
    font-weight: 900;
    color: #68e35f !important;
    margin-bottom: 14px;
    text-transform: uppercase;
}

.estrutura-info {
    border-left: 1px solid rgba(255,255,255,0.22);
    padding-left: 22px;
}

.info-row {
    margin-bottom: 22px;
}

.info-row h4 {
    margin: 0;
    font-size: 16px;
}

.info-row strong {
    font-size: 19px;
}

.info-blue { color: #3f92ff !important; font-weight: 800; }
.info-green { color: #68e35f !important; font-weight: 800; }

.asset-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
}

.asset-table th {
    text-align: left;
    padding: 12px 10px;
    background: rgba(255,255,255,0.05);
    color: rgba(255,255,255,0.85);
}

.asset-table td {
    padding: 13px 10px;
    border-top: 1px solid rgba(255,255,255,0.10);
}

.asset-table td:nth-child(2),
.asset-table td:nth-child(3) {
    text-align: right;
    font-weight: 700;
}

.notice-box {
    margin-top: 14px;
    border: 1px solid rgba(63, 146, 255, 0.45);
    border-radius: 12px;
    padding: 14px;
    background: rgba(0, 80, 150, 0.18);
    color: rgba(255,255,255,0.82);
    font-size: 14px;
}

.highlight-item {
    display: flex;
    gap: 14px;
    align-items: flex-start;
    margin-bottom: 18px;
    line-height: 1.45;
}

.highlight-bullet {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    flex: 0 0 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 900;
}

.highlight-bullet.green {
    background: rgba(76, 190, 76, 0.28);
    color: #67e35e;
}

.highlight-bullet.blue {
    background: rgba(44, 130, 255, 0.28);
    color: #3f92ff;
}

.highlight-bullet.red {
    background: rgba(220, 70, 70, 0.28);
    color: #ff5c5c;
}

.indicator-row {
    display: flex;
    justify-content: space-between;
    gap: 16px;
    padding: 14px 0;
    border-bottom: 1px solid rgba(255,255,255,0.12);
}

.indicator-row:last-child {
    border-bottom: none;
}

.indicator-label {
    font-size: 14px;
    color: rgba(255,255,255,0.84) !important;
}

.indicator-value {
    font-size: 25px;
    font-weight: 900;
}

.indicator-value.green { color: #68e35f !important; }
.indicator-value.blue { color: #3f92ff !important; }

.analysis-card {
    background: rgba(8, 27, 47, 0.72);
    padding: 24px;
    border-radius: 22px;
    border-left: 6px solid #93c5fd;
    min-height: 160px;
    box-shadow: 0 12px 28px rgba(0,0,0,0.20);
}

.good { border-left-color: #22c55e; }
.warning { border-left-color: #f59e0b; }
.info { border-left-color: #38bdf8; }
.risk { border-left-color: #ef4444; }

.glossario-card {
    background: rgba(7, 28, 48, 0.78);
    border: 1px solid rgba(137, 190, 230, 0.28);
    border-radius: 18px;
    padding: 24px;
    box-shadow: 0 14px 30px rgba(0,0,0,0.22);
    margin-bottom: 18px;
}

.glossario-card h3 {
    margin-top: 0;
    color: #68e35f !important;
    font-size: 22px;
}

.glossario-card p {
    color: rgba(255,255,255,0.78) !important;
    line-height: 1.55;
    font-size: 15px;
}

[data-testid="stMetric"] {
    background: #0b2239;
    padding: 26px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 14px 32px rgba(0,0,0,0.26);
}

[data-testid="stMetricValue"] {
    font-size: 2.1rem !important;
}

[data-testid="stDataFrame"] {
    border-radius: 18px;
    overflow: hidden;
}

.pdf-frame {
    width: 100%;
    height: 850px;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 18px;
    background: white;
}

.pdf-card {
    background: rgba(8, 27, 47, 0.72);
    padding: 20px;
    border-radius: 22px;
    border: 1px solid rgba(255,255,255,0.14);
    margin-top: 18px;
    margin-bottom: 24px;
}

.footer {
    text-align: center;
    color: rgba(255,255,255,0.65) !important;
    font-size: 13px;
    margin-top: 24px;
}

hr {
    border-color: rgba(255,255,255,0.22);
}

@media (max-width: 1200px) {
    .kpi-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 800px) {
    .kpi-grid {
        grid-template-columns: 1fr;
    }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNÇÕES
# ============================================================

def grafico_barra(df, x, y, color=None, title=""):
    fig = px.bar(df, x=x, y=y, color=color, text=y, title=title)
    fig.update_traces(texttemplate="R$ %{text:,.2f} Bi", textposition="outside")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(8,27,47,0.45)",
        font_color="white",
        title_font_size=20,
        margin=dict(l=20, r=20, t=60, b=20),
        legend_title_text=""
    )
    return fig


def grafico_pizza(df, names, values, title=""):
    fig = px.pie(df, names=names, values=values, hole=0.55, title=title)
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        title_font_size=20,
        legend_title_text=""
    )
    return fig


def grafico_rosca_estrutura():
    labels = ["Ativo Não Circulante", "Ativo Circulante"]
    values = [8254.52526463, 218.01942971]

    fig = go.Figure(data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=0.62,
            marker=dict(colors=["#58c64f", "#2c83ea"]),
            textinfo="none",
            sort=False
        )
    ])

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        height=260,
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        annotations=[
            dict(
                text="<b>R$ 8,47 Bi</b><br>Ativo Total",
                x=0.5,
                y=0.5,
                font=dict(size=18, color="white"),
                showarrow=False
            )
        ]
    )

    return fig


def grafico_comparativo():
    df = pd.DataFrame({
        "Grupo": [
            "Ativo Total", "Ativo Total",
            "Passivo Exigível", "Passivo Exigível",
            "Patrimônio Líquido", "Patrimônio Líquido"
        ],
        "Ano": ["2025", "2024", "2025", "2024", "2025", "2024"],
        "Valor": [8.47, 8.51, 1.03, 0.85, 7.44, 7.66]
    })

    fig = px.bar(
        df,
        x="Grupo",
        y="Valor",
        color="Ano",
        barmode="group",
        text="Valor",
        color_discrete_map={"2025": "#58c64f", "2024": "#2c83ea"}
    )

    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(8,27,47,0.20)",
        font_color="white",
        height=300,
        margin=dict(l=10, r=10, t=20, b=20),
        legend=dict(orientation="h", y=-0.18, x=0.35),
        yaxis_title="R$ bilhões",
        xaxis_title=""
    )

    return fig


def card_analise(titulo, texto, tipo="info"):
    st.markdown(
        f"""
<div class="analysis-card {tipo}">
<h3>{titulo}</h3>
<p>{texto}</p>
</div>
""",
        unsafe_allow_html=True
    )


def mostrar_pdf(caminho_pdf, titulo="Documento PDF"):
    arquivo = Path(caminho_pdf)

    if not arquivo.exists():
        st.warning(f"PDF não encontrado: {arquivo.name}")
        st.info("Coloque esse arquivo na mesma pasta do app_contabil.py ou ajuste o caminho no código.")
        return

    with open(arquivo, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(f"""
<div class="pdf-card">
<h3>{titulo}</h3>
<iframe class="pdf-frame" src="data:application/pdf;base64,{base64_pdf}" type="application/pdf"></iframe>
</div>
""", unsafe_allow_html=True)

    with open(arquivo, "rb") as f:
        st.download_button(
            label=f"Baixar {titulo}",
            data=f,
            file_name=arquivo.name,
            mime="application/pdf"
        )


def glossario_item(titulo, texto):
    st.markdown(f"""
<div class="glossario-card">
<h3>{titulo}</h3>
<p>{texto}</p>
</div>
""", unsafe_allow_html=True)


def formatar_percentual(valor):
    return f"{valor * 100:.1f}%".replace(".", ",")


# ============================================================
# DADOS
# ============================================================

patrimonial = pd.DataFrame({
    "Grupo": ["Ativo Total", "Passivo", "Patrimônio Líquido"],
    "2024": [8.51, 0.85, 7.66],
    "2025": [8.47, 1.03, 7.44]
})

ativo_comp = pd.DataFrame({
    "Componente": ["Imobilizado", "Caixa e equivalentes", "Créditos", "Estoques", "Demais ativos"],
    "Valor": [6.95, 0.58, 0.41, 0.18, 0.35]
})

orcamentario = pd.DataFrame({
    "Grupo": ["Dotação Atualizada", "Despesa Empenhada", "Despesa Liquidada", "Despesa Paga"],
    "Valor": [4.90, 4.62, 4.41, 4.28]
})

financeiro = pd.DataFrame({
    "Grupo": ["Ingressos", "Dispêndios", "Resultado Financeiro"],
    "Valor": [6.10, 5.95, 0.15]
})

dfc = pd.DataFrame({
    "Atividade": ["Operacional", "Investimentos", "Financiamentos", "Variação Líquida"],
    "Valor": [0.32, -0.085, 0.00, 0.235]
})

dvp = pd.DataFrame({
    "Grupo": ["VPA", "VPD", "Resultado Patrimonial"],
    "Valor": [5.82, 6.04, -0.22065]
})

dotacao = 4.90
empenhado = 4.62
liquidado = 4.41
pago = 4.28

qeoc = empenhado / dotacao
qldc = liquidado / empenhado
qdpc = pago / liquidado


# ============================================================
# MENU
# ============================================================

opcoes_menu = [
    "Resumo Executivo",
    "Análises Patrimoniais",
    "Análises Orçamentárias",
    "Análises Financeiras",
    "Indicadores",
    "Demonstrações Contábeis",
    "Notas Explicativas",
    "Glossário"
]

st.sidebar.markdown("## DCF / UnB")
st.sidebar.markdown("Painel")

if "menu" not in st.session_state:
    st.session_state["menu"] = "Resumo Executivo"

menu = st.sidebar.radio("Menu", opcoes_menu, key="menu")

st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="border:1px solid rgba(255,255,255,0.22); border-radius:14px; padding:18px; margin-top:30px;">
<div style="font-size:14px; color:rgba(255,255,255,0.75);">Atualizado em</div>
<div style="font-weight:800; margin-top:6px;">28/04/2026</div>
<br>
<div style="border:1px solid #53d85a; color:#53d85a; border-radius:10px; padding:12px; text-align:center; font-weight:800;">
Baixar Relatório (PDF)
</div>
</div>
<br><br>
<div style="text-align:center; color:rgba(255,255,255,0.70); font-size:13px;">
Fonte: SIAFI
</div>
""", unsafe_allow_html=True)


# ============================================================
# RESUMO EXECUTIVO
# ============================================================

if menu == "Resumo Executivo":

    st.markdown("""
<div class="dashboard-header">
<div class="dashboard-title">
<h1>DEMONSTRAÇÕES CONTÁBEIS DA UnB</h1>
<p>Exercício 2025 com comparativo 2024</p>
</div>
<div class="exercise-box">Exercício&nbsp;&nbsp;&nbsp; 2025</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="kpi-grid">

<div class="kpi-card">
<div class="kpi-icon green"><div class="kpi-symbol">●</div></div>
<div>
<div class="kpi-label">Ativo Total</div>
<div class="kpi-value green">R$ 8,47 Bi</div>
<div class="kpi-change red">-0,42% &nbsp; <span>vs 2024</span></div>
</div>
</div>

<div class="kpi-card">
<div class="kpi-icon blue"><div class="kpi-symbol">▣</div></div>
<div>
<div class="kpi-label">Passivo Exigível</div>
<div class="kpi-value blue">R$ 1,03 Bi</div>
<div class="kpi-change red">+22,15% &nbsp; <span>vs 2024</span></div>
</div>
</div>

<div class="kpi-card">
<div class="kpi-icon green"><div class="kpi-symbol">✓</div></div>
<div>
<div class="kpi-label">Patrimônio Líquido</div>
<div class="kpi-value green">R$ 7,44 Bi</div>
<div class="kpi-change red">-2,92% &nbsp; <span>vs 2024</span></div>
</div>
</div>

<div class="kpi-card">
<div class="kpi-icon red"><div class="kpi-symbol">↘</div></div>
<div>
<div class="kpi-label">Resultado Patrimonial</div>
<div class="kpi-value red">-R$ 220,65 Mi</div>
<div class="kpi-change red">-145,34% &nbsp; <span>vs 2024</span></div>
</div>
</div>

</div>
""", unsafe_allow_html=True)

    col_estrutura, col_comparativo = st.columns([1.12, 0.95])

    with col_estrutura:
        st.markdown("""
<div class="panel-card">
<div class="panel-title">Estrutura Patrimonial — 2025</div>
""", unsafe_allow_html=True)

        c1, c2 = st.columns([1, 1])

        with c1:
            st.plotly_chart(grafico_rosca_estrutura(), use_container_width=True)

        with c2:
            st.markdown("""
<div class="estrutura-info">
<div class="info-row">
<h4>Ativo Não Circulante</h4>
<strong>R$ 8,25 Bi</strong><br>
<span class="info-green">97,43%</span>
</div>
<div class="info-row">
<h4>Ativo Circulante</h4>
<strong>R$ 218,02 Mi</strong><br>
<span class="info-blue">2,57%</span>
</div>
<hr>
<div class="info-row">
<h4>Passivo Exigível</h4>
<strong>R$ 1,03 Bi</strong><br>
<span class="info-blue">12,20%</span>
</div>
<div class="info-row">
<h4>Patrimônio Líquido</h4>
<strong>R$ 7,44 Bi</strong><br>
<span class="info-green">87,80%</span>
</div>
</div>
""", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with col_comparativo:
        st.markdown("""
<div class="panel-card">
<div class="panel-title">Comparativo 2025 x 2024</div>
""", unsafe_allow_html=True)

        st.plotly_chart(grafico_comparativo(), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    col_tabela, col_destaques, col_indicadores = st.columns([1.05, 0.95, 1.08])

    with col_tabela:
        st.markdown("""
<div class="panel-card">
<div class="panel-title">Composição do Ativo — 2025</div>
<table class="asset-table">
<tr>
<th>Grupo</th>
<th>Valor (R$)</th>
<th>% Part.</th>
</tr>
<tr>
<td>● Ativo Circulante</td>
<td>218.019.429,71</td>
<td>2,57%</td>
</tr>
<tr>
<td>● Ativo Não Circulante</td>
<td>8.254.525.264,63</td>
<td>97,43%</td>
</tr>
<tr>
<td><strong>Total do Ativo</strong></td>
<td><strong>8.472.544.694,34</strong></td>
<td><strong>100,00%</strong></td>
</tr>
</table>
<div class="notice-box">
O Ativo Não Circulante representa 97,43% do total do ativo, com destaque para bens móveis e imóveis.
</div>
</div>
""", unsafe_allow_html=True)

    with col_destaques:
        st.markdown("""
<div class="panel-card">
<div class="panel-title">Destaques do Exercício</div>
<div class="highlight-item">
<div class="highlight-bullet green">↗</div>
<div>O ativo total apresentou redução de 0,42% em relação a 2024.</div>
</div>
<div class="highlight-item">
<div class="highlight-bullet blue">▣</div>
<div>O passivo exigível aumentou 22,15%, principalmente por obrigações trabalhistas.</div>
</div>
<div class="highlight-item">
<div class="highlight-bullet green">✓</div>
<div>O patrimônio líquido reduziu 2,92%, impactado pelo resultado patrimonial negativo.</div>
</div>
<div class="highlight-item">
<div class="highlight-bullet red">↘</div>
<div>O resultado patrimonial de 2025 foi deficitário em R$ 220,65 milhões.</div>
</div>
</div>
""", unsafe_allow_html=True)

    with col_indicadores:
        st.markdown("""
<div class="panel-card">
<div class="panel-title">Indicadores Patrimoniais</div>
<div class="indicator-row">
<div class="indicator-label">Participação do PL no Ativo<br>(PL / Ativo Total)</div>
<div class="indicator-value green">87,80%</div>
</div>
<div class="indicator-row">
<div class="indicator-label">Participação do Passivo no Ativo<br>(Passivo / Ativo Total)</div>
<div class="indicator-value blue">12,20%</div>
</div>
<div class="indicator-row">
<div class="indicator-label">Liquidez Corrente<br>(Ativo Circulante / Passivo Circulante)</div>
<div class="indicator-value green">0,21</div>
</div>
<div class="indicator-row">
<div class="indicator-label">Imobilização do Patrimônio<br>(Ativo Não Circulante / PL)</div>
<div class="indicator-value green">1,11</div>
</div>
</div>
""", unsafe_allow_html=True)

    st.markdown("""
<div class="footer">
UnB — Fundação Universidade de Brasília &nbsp; | &nbsp; Diretoria de Contabilidade e Finanças — DCF
</div>
""", unsafe_allow_html=True)


# ============================================================
# DEMAIS PÁGINAS
# ============================================================

else:

    st.markdown("""
<div class="bloco">
<h1>Demonstrações Contábeis da UnB</h1>
<p>Exercício 2025 com comparativo 2024</p>
</div>
""", unsafe_allow_html=True)

    if menu == "Análises Patrimoniais":

        st.header("Análises Patrimoniais")

        col1, col2, col3 = st.columns(3)
        col1.metric("Ativo Total", "R$ 8,47 Bi", "-R$ 40 Mi")
        col2.metric("Passivo", "R$ 1,03 Bi", "+R$ 180 Mi")
        col3.metric("Patrimônio Líquido", "R$ 7,44 Bi", "-R$ 220 Mi")

        st.divider()

        col_a, col_b = st.columns([1.2, 1])

        with col_a:
            st.plotly_chart(
                grafico_barra(
                    patrimonial.melt(id_vars="Grupo", var_name="Ano", value_name="Valor"),
                    x="Grupo",
                    y="Valor",
                    color="Ano",
                    title="Evolução patrimonial"
                ),
                use_container_width=True
            )

        with col_b:
            st.plotly_chart(
                grafico_pizza(
                    ativo_comp,
                    names="Componente",
                    values="Valor",
                    title="Composição do Ativo"
                ),
                use_container_width=True
            )

        st.subheader("Análises")

        c1, c2 = st.columns(2)

        with c1:
            card_analise(
                "Predominância de ativos permanentes",
                "A maior parcela do ativo está associada ao imobilizado, o que reforça a importância dos controles patrimoniais, inventários e reavaliação das informações cadastrais.",
                "info"
            )

        with c2:
            card_analise(
                "Baixa pressão relativa do passivo",
                "O passivo representa proporção menor frente ao ativo total, mantendo relação patrimonial favorável no encerramento do exercício.",
                "good"
            )

        c3, c4 = st.columns(2)

        with c3:
            card_analise(
                "Necessidade de evidenciação",
                "A qualidade das notas explicativas é essencial para demonstrar critérios de mensuração, composição dos bens e eventuais limitações dos registros.",
                "warning"
            )

        with c4:
            card_analise(
                "Patrimônio líquido positivo",
                "A diferença positiva entre ativos e passivos demonstra situação líquida patrimonial favorável, apesar da redução no comparativo anual.",
                "good"
            )


    elif menu == "Análises Orçamentárias":

        st.header("Análises Orçamentárias")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Dotação Atualizada", "R$ 4,90 Bi")
        col2.metric("Empenhado", "R$ 4,62 Bi", "94,3%")
        col3.metric("Liquidado", "R$ 4,41 Bi", "95,5% do empenhado")
        col4.metric("Pago", "R$ 4,28 Bi", "97,1% do liquidado")

        st.divider()

        st.plotly_chart(
            grafico_barra(
                orcamentario,
                x="Grupo",
                y="Valor",
                color="Grupo",
                title="Estágios da execução orçamentária"
            ),
            use_container_width=True
        )

        st.subheader("Análises")

        c1, c2 = st.columns(2)

        with c1:
            card_analise(
                "Alto nível de empenho",
                "O percentual empenhado indica forte comprometimento da dotação atualizada, demonstrando elevada execução orçamentária no exercício.",
                "good"
            )

        with c2:
            card_analise(
                "Monitoramento da liquidação",
                "A relação entre empenho e liquidação deve ser acompanhada para reduzir saldos pendentes e melhorar a qualidade da execução.",
                "warning"
            )

        c3, c4 = st.columns(2)

        with c3:
            card_analise(
                "Pagamentos próximos da liquidação",
                "O volume pago em relação ao liquidado sugere bom andamento do fluxo de pagamento, condicionado à disponibilidade financeira.",
                "info"
            )

        with c4:
            card_analise(
                "Risco de restos a pagar",
                "Eventuais diferenças entre empenhado, liquidado e pago devem ser acompanhadas para mitigar crescimento de restos a pagar.",
                "risk"
            )


    elif menu == "Análises Financeiras":

        st.header("Análises Financeiras")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Ingressos", "R$ 6,10 Bi")
        col2.metric("Dispêndios", "R$ 5,95 Bi")
        col3.metric("Resultado Financeiro", "R$ 150 Mi")
        col4.metric("Variação de Caixa", "R$ 235 Mi")

        st.divider()

        col_a, col_b = st.columns(2)

        with col_a:
            st.plotly_chart(
                grafico_barra(
                    financeiro,
                    x="Grupo",
                    y="Valor",
                    color="Grupo",
                    title="Balanço Financeiro — síntese"
                ),
                use_container_width=True
            )

        with col_b:
            st.plotly_chart(
                grafico_barra(
                    dfc,
                    x="Atividade",
                    y="Valor",
                    color="Atividade",
                    title="Fluxos de Caixa — síntese"
                ),
                use_container_width=True
            )

        st.subheader("Análises")

        c1, c2 = st.columns(2)

        with c1:
            card_analise(
                "Resultado financeiro positivo",
                "Os ingressos superaram os dispêndios no exercício, indicando equilíbrio financeiro no período analisado.",
                "good"
            )

        with c2:
            card_analise(
                "Fluxo operacional positivo",
                "A geração operacional de caixa é o principal elemento de sustentação da variação positiva de caixa.",
                "info"
            )

        c3, c4 = st.columns(2)

        with c3:
            card_analise(
                "Investimentos com saída líquida",
                "A saída em investimentos é compatível com aplicação de recursos em bens e infraestrutura, devendo ser analisada junto à política patrimonial.",
                "warning"
            )

        with c4:
            card_analise(
                "Capacidade de pagamento",
                "A variação positiva de caixa contribui para a capacidade de honrar obrigações, observadas as vinculações e restrições de recursos.",
                "good"
            )


    elif menu == "Indicadores":

        st.header("Indicadores")

        st.markdown("""
<div class="bloco">
Esta página apresenta indicadores patrimoniais, orçamentários, operacionais e financeiros para apoio à leitura gerencial das demonstrações contábeis.
</div>
""", unsafe_allow_html=True)

        st.subheader("Indicadores de Execução da Despesa")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "QEOC",
                formatar_percentual(qeoc),
                "Empenhado / Dotação"
            )

        with col2:
            st.metric(
                "QLDC",
                formatar_percentual(qldc),
                "Liquidado / Empenhado"
            )

        with col3:
            st.metric(
                "QDPC",
                formatar_percentual(qdpc),
                "Pago / Liquidado"
            )

        st.divider()

        indicadores_exec = pd.DataFrame({
            "KPI": [
                "QEOC",
                "QLDC",
                "QDPC"
            ],
            "Denominação": [
                "Quociente da Execução Orçamentária da Despesa Corrente",
                "Quociente da Liquidação da Despesa Corrente",
                "Quociente da Despesa Corrente Paga"
            ],
            "Fórmula": [
                "Despesa Empenhada / Dotação Atualizada",
                "Despesa Liquidada / Despesa Empenhada",
                "Despesa Paga / Despesa Liquidada"
            ],
            "Valor": [
                formatar_percentual(qeoc),
                formatar_percentual(qldc),
                formatar_percentual(qdpc)
            ],
            "Meta de Referência": [
                "≥ 90%",
                "≥ 90%",
                "≥ 90%"
            ],
            "Finalidade Gerencial": [
                "Monitorar o comprometimento da dotação disponível",
                "Avaliar a efetividade da liquidação da despesa",
                "Monitorar o cumprimento financeiro das despesas liquidadas"
            ]
        })

        st.dataframe(indicadores_exec, use_container_width=True, hide_index=True)

        st.divider()

        st.subheader("Análise Gerencial dos Indicadores de Execução")

        col_a, col_b, col_c = st.columns(3)

        with col_a:
            card_analise(
                "Execução Orçamentária",
                f"O QEOC alcançou {formatar_percentual(qeoc)}, indicando elevado comprometimento da dotação atualizada em relação ao volume empenhado.",
                "good"
            )

        with col_b:
            card_analise(
                "Eficiência Operacional",
                f"O QLDC alcançou {formatar_percentual(qldc)}, demonstrando boa conversão da despesa empenhada em despesa liquidada.",
                "info"
            )

        with col_c:
            card_analise(
                "Fluxo Financeiro",
                f"O QDPC alcançou {formatar_percentual(qdpc)}, indicando regularidade no pagamento das despesas já liquidadas.",
                "good"
            )

        st.divider()

        st.subheader("Indicadores Consolidados")

        indicadores = pd.DataFrame({
            "Indicador": [
                "Passivo / Ativo",
                "Patrimônio Líquido / Ativo",
                "Empenhado / Dotação",
                "Liquidado / Empenhado",
                "Pago / Liquidado",
                "Resultado Financeiro / Ingressos"
            ],
            "Valor": [
                "12,2%",
                "87,8%",
                formatar_percentual(qeoc),
                formatar_percentual(qldc),
                formatar_percentual(qdpc),
                "2,5%"
            ],
            "Leitura": [
                "Baixa pressão relativa do passivo",
                "Elevada participação do patrimônio líquido",
                "Alta execução orçamentária",
                "Boa conversão do empenho em liquidação",
                "Boa conversão da liquidação em pagamento",
                "Resultado financeiro positivo"
            ]
        })

        st.dataframe(indicadores, use_container_width=True, hide_index=True)

        st.divider()

        c1, c2, c3 = st.columns(3)
        c1.metric("Passivo / Ativo", "12,2%", "Baixo")
        c2.metric("PL / Ativo", "87,8%", "Alto")
        c3.metric("Pago / Liquidado", formatar_percentual(qdpc), "Bom")

        st.subheader("Síntese dos indicadores")

        card_analise(
            "Leitura consolidada",
            "Os indicadores sugerem estrutura patrimonial favorável, execução orçamentária elevada e boa conversão da despesa liquidada em pagamento.",
            "good"
        )


    elif menu == "Demonstrações Contábeis":

        st.header("Demonstrações Contábeis")

        st.markdown("""
<div class="bloco">
Esta página concentra as demonstrações contábeis em formato PDF para consulta direta.
Cada aba apresenta a demonstração correspondente.
</div>
""", unsafe_allow_html=True)

        aba1, aba2, aba3, aba4, aba5 = st.tabs([
            "Balanço Patrimonial",
            "DVP",
            "Balanço Financeiro",
            "DFC",
            "Balanço Orçamentário"
        ])

        with aba1:
            mostrar_pdf("balanco_patrimonial.pdf", "Balanço Patrimonial")

        with aba2:
            mostrar_pdf("dvp.pdf", "Demonstração das Variações Patrimoniais - DVP")

        with aba3:
            mostrar_pdf("balanco_financeiro.pdf", "Balanço Financeiro")

        with aba4:
            mostrar_pdf("dfc.pdf", "Demonstração dos Fluxos de Caixa - DFC")

        with aba5:
            mostrar_pdf("balanco_orcamentario.pdf", "Balanço Orçamentário")


    elif menu == "Notas Explicativas":

        st.header("Notas Explicativas")

        st.markdown("""
<div class="bloco">
Esta página apresenta o documento completo das Notas Explicativas das Demonstrações Contábeis.
</div>
""", unsafe_allow_html=True)

        mostrar_pdf("notas_explicativas.pdf", "Notas Explicativas")


    elif menu == "Glossário":

        st.header("Glossário Contábil e Financeiro")

        st.markdown("""
<div class="bloco">
Esta página apresenta conceitos básicos usados no painel, com linguagem acessível para apoiar a leitura das demonstrações contábeis.
</div>
""", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            glossario_item(
                "Ativo Total",
                "Representa o conjunto de bens, direitos e demais recursos controlados pela Universidade. Inclui caixa, créditos, estoques, bens móveis, imóveis e outros ativos."
            )

            glossario_item(
                "Ativo Circulante",
                "Compreende os recursos realizáveis no curto prazo, como caixa, equivalentes de caixa, créditos a receber e outros valores que podem ser convertidos em recursos em menor prazo."
            )

            glossario_item(
                "Ativo Não Circulante",
                "Representa os ativos de longo prazo, como bens móveis, imóveis, investimentos, intangíveis e outros elementos que permanecem na entidade por período mais longo."
            )

            glossario_item(
                "Passivo Exigível",
                "Corresponde às obrigações presentes da entidade, como fornecedores, encargos, obrigações trabalhistas, previdenciárias e demais compromissos reconhecidos contabilmente."
            )

            glossario_item(
                "Patrimônio Líquido",
                "É a diferença entre o Ativo e o Passivo. No setor público, evidencia a situação líquida patrimonial acumulada da entidade."
            )

            glossario_item(
                "Resultado Patrimonial",
                "É a diferença entre as Variações Patrimoniais Aumentativas e as Variações Patrimoniais Diminutivas. Pode indicar superávit ou déficit patrimonial."
            )

            glossario_item(
                "DVP",
                "A Demonstração das Variações Patrimoniais evidencia as alterações que aumentaram ou diminuíram o patrimônio durante o exercício."
            )

            glossario_item(
                "VPA",
                "Variações Patrimoniais Aumentativas. Representam eventos que aumentam o patrimônio, como receitas, transferências recebidas e outros acréscimos patrimoniais."
            )

            glossario_item(
                "QEOC",
                "Quociente da Execução Orçamentária da Despesa Corrente. Mede a relação entre a despesa empenhada e a dotação atualizada, indicando o nível de comprometimento orçamentário."
            )

            glossario_item(
                "QLDC",
                "Quociente da Liquidação da Despesa Corrente. Mede a relação entre a despesa liquidada e a despesa empenhada, indicando a efetividade operacional da execução."
            )

        with col2:
            glossario_item(
                "VPD",
                "Variações Patrimoniais Diminutivas. Representam eventos que reduzem o patrimônio, como despesas, depreciação, perdas e outras diminuições patrimoniais."
            )

            glossario_item(
                "Balanço Financeiro",
                "Demonstra os ingressos e dispêndios financeiros do exercício, evidenciando a movimentação financeira da entidade."
            )

            glossario_item(
                "DFC",
                "A Demonstração dos Fluxos de Caixa apresenta os fluxos de entrada e saída de caixa classificados por atividades operacionais, de investimento e financiamento."
            )

            glossario_item(
                "Balanço Orçamentário",
                "Compara as receitas e despesas previstas com as efetivamente realizadas, permitindo avaliar a execução orçamentária."
            )

            glossario_item(
                "Empenho",
                "É o primeiro estágio da despesa pública. Representa a reserva de dotação orçamentária para uma obrigação assumida pela administração."
            )

            glossario_item(
                "Liquidação",
                "É o estágio em que se verifica o direito adquirido pelo credor, com base em documentos que comprovem a entrega do bem ou a prestação do serviço."
            )

            glossario_item(
                "Pagamento",
                "É o estágio final da despesa pública, quando ocorre a efetiva saída de recursos financeiros para quitar a obrigação."
            )

            glossario_item(
                "Restos a Pagar",
                "São despesas empenhadas e não pagas até o encerramento do exercício. Podem ser processados ou não processados, conforme tenham sido liquidados ou não."
            )

            glossario_item(
                "QDPC",
                "Quociente da Despesa Corrente Paga. Mede a relação entre a despesa paga e a despesa liquidada, indicando o grau de cumprimento financeiro das obrigações já liquidadas."
            )

            glossario_item(
                "Meta de Referência ≥ 90%",
                "Parâmetro gerencial utilizado para avaliar se os indicadores de execução, liquidação e pagamento apresentam desempenho considerado adequado."
            )

        col3, col4 = st.columns(2)

        with col3:
            glossario_item(
                "Passivo / Ativo",
                "Indicador que mostra a participação das obrigações em relação ao total de ativos. Quanto maior, maior a pressão das obrigações sobre o patrimônio."
            )

            glossario_item(
                "PL / Ativo",
                "Indicador que mostra quanto do ativo é financiado pelo patrimônio líquido. No painel, ajuda a visualizar a predominância do patrimônio líquido na estrutura patrimonial."
            )

            glossario_item(
                "Liquidez Corrente",
                "Indicador que relaciona Ativo Circulante e Passivo Circulante. Ajuda a avaliar a capacidade de cumprir obrigações de curto prazo com recursos de curto prazo."
            )

            glossario_item(
                "Dotação Atualizada",
                "Valor autorizado no orçamento após alterações orçamentárias, como créditos adicionais, cancelamentos e remanejamentos."
            )

        with col4:
            glossario_item(
                "Imobilização do Patrimônio",
                "Indicador que relaciona o Ativo Não Circulante com o Patrimônio Líquido, mostrando quanto do patrimônio está aplicado em ativos de longo prazo."
            )

            glossario_item(
                "Empenhado / Dotação",
                "Indicador que mede o percentual da dotação orçamentária já comprometido por meio de empenhos emitidos."
            )

            glossario_item(
                "Liquidado / Empenhado",
                "Indicador que mede a parcela da despesa empenhada que já foi efetivamente liquidada, ou seja, reconhecida como obrigação a pagar."
            )

            glossario_item(
                "Pago / Liquidado",
                "Indicador que mede a parcela da despesa liquidada que já foi paga, demonstrando a regularidade do fluxo financeiro."
            )

            glossario_item(
                "Notas Explicativas",
                "Documento complementar às demonstrações contábeis. Explica critérios, saldos relevantes, eventos significativos e informações necessárias para melhor compreensão dos demonstrativos."
            )