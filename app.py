import streamlit as st
from graphviz import Digraph

st.set_page_config(layout="centered")

# Nomes fixos para os nós
nodes = ["A", "B", "C", "D", "E", "F", "G"]

def build_tree(inputs, tree_id):
    dot = Digraph()
    color = "black"
    
    edges = [
        ("A", "B"), ("A", "C"),
        ("B", "D"), ("B", "E"),
        ("C", "F"), ("C", "G")
    ]

    for node in nodes:
        value = inputs.get(f"{tree_id}_{node}", "")
        color = "black"
        if f"{tree_id}_{node}_color" in inputs:
            color = inputs[f"{tree_id}_{node}_color"]
        dot.node(f"{tree_id}_{node}", str(value), style="filled", fillcolor=color, fontcolor="white" if color == "green" else "black")

    for a, b in edges:
        dot.edge(f"{tree_id}_{a}", f"{tree_id}_{b}")

    return dot


def compare_trees(inputs1, inputs2):
    result_colors_1 = {}
    result_colors_2 = {}

    for node in nodes:
        val1 = inputs1.get(f"tree1_{node}", 0)
        val2 = inputs2.get(f"tree2_{node}", 0)

        if val1 > val2:
            result_colors_1[f"tree1_{node}_color"] = "green"
            result_colors_2[f"tree2_{node}_color"] = "black"
        elif val2 > val1:
            result_colors_2[f"tree2_{node}_color"] = "green"
            result_colors_1[f"tree1_{node}_color"] = "black"
        else:
            result_colors_1[f"tree1_{node}_color"] = "black"
            result_colors_2[f"tree2_{node}_color"] = "black"

    return result_colors_1, result_colors_2

st.title("Comparador de Árvores Binárias")

st.subheader("Preencha os valores da Árvore 1")
tree1_inputs = {}
for node in nodes:
    tree1_inputs[f"tree1_{node}"] = st.number_input(f"Árvore 1 - Nó {node}", key=f"tree1_{node}", step=1)

st.subheader("Preencha os valores da Árvore 2")
tree2_inputs = {}
for node in nodes:
    tree2_inputs[f"tree2_{node}"] = st.number_input(f"Árvore 2 - Nó {node}", key=f"tree2_{node}", step=1)

if st.button("Comparar Árvores"):
    colors1, colors2 = compare_trees(tree1_inputs, tree2_inputs)
    tree1_inputs.update(colors1)
    tree2_inputs.update(colors2)

    st.subheader("Resultado - Árvore 1")
    st.graphviz_chart(build_tree(tree1_inputs, "tree1"))

    st.subheader("Resultado - Árvore 2")
    st.graphviz_chart(build_tree(tree2_inputs, "tree2"))
