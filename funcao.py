import mysql.connector as my

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
    ''' Faz a inserção de um produto no banco de dados. A imagem é a URL da imagem do produto na web.
        Utilizar formatos encurtados com quantidade de caracteres inferiores a 100
        Você poderá usar o https://www.encurtarlink.com/ para ajustar ao formato adequado'''
    conexao, cursor = conectarbd()
    comandoSQL = f'INSERT INTO produtos (nome, preco, id, imagem) VALUES ({nome}, {preco}, {id}, {img})'

    cursor.execute(comandoSQL)
    conexao.commit() # aqui é onde vamos inserir os dados
    print("Produto cadastrado com sucesso")
    conexao.close()

# funcao selecionar
def selecionartdprodutos():
    conexao,cursor = conectarbd()
    comandoSQL = f"SELECT id, nome, preco FROM produtos"
    cursor.execute(comandoSQL)
    resultado_consulta = cursor.fetchall()
    return resultado_consulta

#Função atualizar
def atualizarpeco(id: str, novo_valor: float):
    conexao,cursor = conectarbd()
    comandoSQL = f'UPDATE produtos SET preco = {novo_valor} WHERE id = "{id}"'
    cursor.execute(comandoSQL)
    conexao.commit()

#função deletar
def deletar(id:str):
    conexao,cursor = conectarbd()
    comandoSQL = f'DELETE FROM produtos WHERE id = "{id}"'
    cursor.execute(comandoSQL)
    conexao.commit()
