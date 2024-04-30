import streamlit as st
from funcao import cadastrar

st.title("Tela do banco de dados :alien:")
st.header("Sistema de produtos")
st.markdown("##Cadastro produtos")

st.write("Esse programa foi desenvolvido como teste")



nome = st.text_input("Nome do produto", placeholder="max 50 caracteres")
preco = float(st.number_input("Digite o valor do produto: "))
imagem = st.text_input("imagem do produto", placeholder="url da imagem produto de até 100 caract")
codigo = st.text_input("Código do produto:", placeholder="codigo do produto")

btncadastro = st.button("Cadastrar produto")

if btncadastro:
    cadastrar(nome, preco, codigo, imagem)
    st.write("Cadastro feito com sucesso")

