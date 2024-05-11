import streamlit as st
import pandas as pd
from funcao import cadastrar
from funcao import atualizarpeco
from funcao import deletar
from funcao import selecionarTodosProdutos
from funcao import *

st.title("Tela do banco de dados :alien:")

col1, col2 = st.columns(2)

containercadastrar = col1.container(border=True)
containeatualizar = col2.container(border=True)

containercadastrar.header("Cadastro produtos")

with containercadastrar:
    st.write("Esse programa foi desenvolvido como teste")

    nome = st.text_input("Nome do produto", placeholder="max 50 caracteres")
    preco = float(st.number_input("Digite o valor do produto: "))
    imagem = st.text_input("imagem do produto", placeholder="url da imagem produto de até 100 caract")
    codigo = st.text_input("Código do produto:", placeholder="codigo do produto")

    btncadastro = st.button("Cadastrar produto")

    if btncadastro:
        cadastrar(nome, preco, codigo, imagem)
        st.write("Cadastro feito com sucesso")

st.markdown("----------------------------------------")


containeatualizar.header("Atualização do valor")

with containeatualizar:
    novo_nome = st.text_input("Novo nome produto: ")
    novo_valor = float(st.number_input("Digite o novo valor do produto: "))
    id = st.text_input("Código do produto", placeholder="codigo do produto")

    btnatualizarpreco = st.button("Atualizar preço")

    if btnatualizarpreco:
        atualizarpeco(id, novo_valor)
        st.write("Preço atualizado")
col3, col4 = st.columns(2)

st.markdown("---------------------------------------")
containerListar = st.expander('Todos os produtos')

with containerListar:
    listaProdutos = selecionarTodosProdutos()
    st.title('Todos os produtos')
    tabelaPodutos = pd.DataFrame(listaProdutos, columns=('id', 'nome', 'preço'))
    st.write(tabelaPodutos)

    btnlistarprodutos = st.button('mostrar produto')

    if btnlistarprodutos:
        listaProdutos(id, nome, preco)
        st.write("listar")


col3, col4 = st.columns(2)
containerUmProduto = col3.container(border=True)

with containerUmProduto:
    containerUmProduto.markdown('## Listar um produto')
    codigoDoProduto = st.text_input('Codigo do produto a ser listado')

    btnmostrar_produtos = st.button("mostrar item")

    if btnmostrar_produtos:
        listaProdutos(id)
        st.write("mostrar")