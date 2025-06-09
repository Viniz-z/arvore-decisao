import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Árvore Interativa", layout="wide")

html_code = """
<div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
  <div style="text-align: center;">
    <h3>Árvore 1</h3>
    <div id="arvore1" style="display: flex; flex-direction: column; align-items: center;">
      """ + ''.join(f'<button onclick="editarValor(this, 1, {i})" class="no" id="no1-{i}">0</button>' for i in range(7)) + """
    </div>
  </div>
  <div style="text-align: center;">
    <h3>Árvore 2</h3>
    <div id="arvore2" style="display: flex; flex-direction: column; align-items: center;">
      """ + ''.join(f'<button onclick="editarValor(this, 2, {i})" class="no" id="no2-{i}">0</button>' for i in range(7)) + """
    </div>
  </div>
</div>

<style>
  .no {
    margin: 5px;
    padding: 15px;
    border-radius: 50%;
    border: 2px solid #000;
    background-color: lightgray;
    font-weight: bold;
    width: 50px;
    height: 50px;
    font-size: 16px;
  }
  .verde {
    background-color: #a6e6a1 !important;
    border-color: green;
  }
</style>

<script>
  function editarValor(elem, arvore, index) {
    let novo = prompt("Novo valor:", elem.innerText);
    if (novo !== null) {
      novo = parseFloat(novo);
      if (!isNaN(novo)) {
        elem.innerText = novo;
        comparar();
      }
    }
  }

  function comparar() {
    for (let i = 0; i < 7; i++) {
      let no1 = document.getElementById("no1-" + i);
      let no2 = document.getElementById("no2-" + i);
      let v1 = parseFloat(no1.innerText);
      let v2 = parseFloat(no2.innerText);

      no1.classList.remove("verde");
      no2.classList.remove("verde");

      if (!isNaN(v1) && !isNaN(v2)) {
        if (v1 > v2) no1.classList.add("verde");
        else if (v2 > v1) no2.classList.add("verde");
      }
    }
  }

  setTimeout(comparar, 100);
</script>
"""

components.html(html_code, height=600)
