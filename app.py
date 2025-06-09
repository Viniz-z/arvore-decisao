import streamlit as st
import uuid

st.set_page_config(page_title="Comparador de Árvores", layout="wide")
st.title("🌳 Comparador de Árvores Binárias")

# Inicializa valores e títulos no estado da sessão
if "arvore1" not in st.session_state:
    st.session_state.arvore1 = [""] * 7
if "arvore2" not in st.session_state:
    st.session_state.arvore2 = [""] * 7

if "titulos_arvore1" not in st.session_state:
    st.session_state.titulos_arvore1 = [f"Nó {i+1}" for i in range(7)]
if "titulos_arvore2" not in st.session_state:
    st.session_state.titulos_arvore2 = [f"Nó {i+1}" for i in range(7)]

# Função para criar input do valor do nó
def input_no_valor(id_arvore, i, valor):
    key = f"{id_arvore}-valor-{i}-{uuid.uuid4()}"
    return st.text_input(f"Valor {i+1}", value=valor, key=key, max_chars=3)

# Função para criar input do título do nó
def input_no_titulo(id_arvore, i, titulo):
    key = f"{id_arvore}-titulo-{i}-{uuid.uuid4()}"
    return st.text_input(f"Título {i+1}", value=titulo, key=key)

# Inputs para árvore 1
st.subheader("Árvore 1")
for i in range(7):
    st.session_state.arvore1[i] = input_no_valor("arvore1", i, st.session_state.arvore1[i])
for i in range(7):
    st.session_state.titulos_arvore1[i] = input_no_titulo("arvore1", i, st.session_state.titulos_arvore1[i])

# Inputs para árvore 2
st.subheader("Árvore 2")
for i in range(7):
    st.session_state.arvore2[i] = input_no_valor("arvore2", i, st.session_state.arvore2[i])
for i in range(7):
    st.session_state.titulos_arvore2[i] = input_no_titulo("arvore2", i, st.session_state.titulos_arvore2[i])

# Compara valores para cores
cores1 = [""] * 7
cores2 = [""] * 7
for i in range(7):
    try:
        n1 = float(st.session_state.arvore1[i])
        n2 = float(st.session_state.arvore2[i])
        if n1 > n2:
            cores1[i] = "green"
            cores2[i] = ""
        elif n2 > n1:
            cores2[i] = "green"
            cores1[i] = ""
        else:
            cores1[i] = cores2[i] = ""
    except:
        cores1[i] = cores2[i] = ""

# Função para desenhar árvore com títulos dinâmicos
def desenhar_arvore(id_arvore, valores, cores, titulos):
    st.markdown(f"""
    <style>
        .container-{id_arvore} {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 40px;
        }}
        .linha {{
            display: flex;
            justify-content: center;
            margin: 5px 0;
        }}
        .no {{
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 2px solid #333;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 8px;
            font-weight: bold;
            background-color: lightgray;
            cursor: default;
        }}
        .no.verde {{
            background-color: #a6e6a1;
            border-color: green;
        }}
    </style>

    <div class="container-{id_arvore}">
        <div class="linha">
            <div class="no {'verde' if cores[0] == 'green' else ''}" title="{titulos[0]}">{valores[0]}</div>
        </div>
        <div class="linha">
            <div class="no {'verde' if cores[1] == 'green' else ''}" title="{titulos[1]}">{valores[1]}</div>
            <div class="no {'verde' if cores[2] == 'green' else ''}" title="{titulos[2]}">{valores[2]}</div>
        </div>
        <div class="linha">
            <div class="no {'verde' if cores[3] == 'green' else ''}" title="{titulos[3]}">{valores[3]}</div>
            <div class="no {'verde' if cores[4] == 'green' else ''}" title="{titulos[4]}">{valores[4]}</div>
            <div class="no {'verde' if cores[5] == 'green' else ''}" title="{titulos[5]}">{valores[5]}</div>
            <div class="no {'verde' if cores[6] == 'green' else ''}" title="{titulos[6]}">{valores[6]}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Visualização Árvore 1")
    desenhar_arvore("arvore1", st.session_state.arvore1, cores1, st.session_state.titulos_arvore1)

with col2:
    st.subheader("Visualização Árvore 2")
    desenhar_arvore("arvore2", st.session_state.arvore2, cores2, st.session_state.titulos_arvore2)
