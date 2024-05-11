import mysql.connector as my
import mysql

def conectarbd():
    conexao = my.connect(
        host="localhost",
        user="root",
        password="",
        database="loja"
    )

    cursor = conexao.cursor()
    print("conexão estabelecida")
    return conexao,cursor

#função inserir
def cadastrar(nome: str, preco: float, id: str, img: str):
    conexao, cursor = conectarbd()
    comandoSQL = f'INSERT INTO produtos (nome, preco, id, imagem) VALUES ("{nome}", {preco}, "{id}", "{img}")'

    cursor.execute(comandoSQL)
    conexao.commit() # aqui é onde vamos inserir os dados
    print("Produto cadastrado com sucesso")
    conexao.close()

#Função atualizar
def atualizarpeco(id: str, novo_valor: float):
    conexao, cursor = conectarbd()
    comandoSQL = f'UPDATE produtos SET preco = {novo_valor} WHERE id = "{id}"'
    cursor.execute(comandoSQL)
    conexao.commit()

#Função listartodos

def selecionarTodosProdutos():
    conexao, cursor = conectarbd()
    comando_sql = f'select id, nome, preco from produtos'
    cursor.execute(comando_sql)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta

#função deletar
def deletar(id: str):
    conexao, cursor = conectarbd()
    comandoSQL = f'DELETE FROM produtos WHERE id = "{id}"'
    cursor.execute(comandoSQL)
    conexao.commit()