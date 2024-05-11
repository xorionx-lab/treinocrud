import streamlit as st
import pandas as pd

from funcao import *

# cadastro
st.title('Sistema Dieguinho Alimentos - ME')

col1, col2 = st.columns(2)

containerCadastrar = col1.container(border=True)
containerAlterar = col2.container(border=True)

with containerCadastrar:
    containerCadastrar.markdown('## Cadastro de Produtos')
    nome = st.text_input('Nome do produto', placeholder='Nome do produto com no máximo 50 caracteres')
    imagem = st.text_input('Imagem do produto', placeholder='Url da imagem do produto com até 100 caracteres')
    codigo = st.text_input('Código do produto', placeholder='Código do produto')
    preco = float(st.number_input('Preço produto'))
    btnCadastrarProduto = st.button('Cadastrar Produto')
    if btnCadastrarProduto:
        cadastrar(nome, preco, codigo, imagem)
        st.write('Produto cadastrado com sucesso')

with containerAlterar:
    containerAlterar.markdown('## Alterar Produto')
    novoNome = st.text_input('Novo nome produto')
    novoPreco= st.number_input('Novo preço')
    idProduto= st.text_input('Código do produto original')
    novaImagem = st.text_input('Nova Imagem produto')
    st.button('Alterar produto')

containerListar = st.expander('Todos os produtos')


with containerListar:
    listaProdutos = selecionarTodosProdutos()
    st.title('Todos os produtos')
    tabelaPodutos = pd.DataFrame(listaProdutos, columns=('id', 'nome', 'preço'))
    st.write(tabelaPodutos)

col3, col4 = st.columns(2)
containerUmProduto = col3.container(border=True)

with containerUmProduto:
    containerUmProduto.markdown('## Listar um produto')
    codigoDoProduto = st.text_input('Codigo do produto a ser listado')
    btnProcurarProduto = st.button('Procurar produtro')

    if btnProcurarProduto:
        produtoSelecionado = selecionarUmProduto(codigoDoProduto)

        if produtoSelecionado:
            st.write(produtoSelecionado)
            st.image(produtoSelecionado[3])